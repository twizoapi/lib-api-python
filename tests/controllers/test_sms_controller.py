import json
import unittest
from unittest.mock import MagicMock, call

from controllers import SmsController
from enums import RequestType
from exceptions import TwizoParamsException, TwizoDataException
from models import TwizoModel
from models.parameters import SmsParams, SmsAdvanceParams
from service import TwizoService
from worker import Worker


class SmsControllerTest(unittest.TestCase):
    def setUp(self):
        self.worker_mock = Worker("", "")
        self.worker_mock.execute = MagicMock()
        self.service_mock = TwizoService()
        self.service_mock.parse = MagicMock()

        self.sut = SmsController(self.worker_mock, self.service_mock)

    def test_send_simple(self):
        expected = ["123456"], "body", "sender"

        # Execute method
        params = SmsParams(*expected)
        self.sut.send_simple(params)

        self.worker_mock.execute.assert_called_once_with(
            url="sms/submitsimple",
            parameters=json.dumps(params.__dict__),
            request_type=RequestType.POST,
            expected_status=201
        )

        self.service_mock.parse.assert_called_once()

    def test_send_simple_EmptyParam(self):
        with self.assertRaisesRegex(TwizoParamsException, "Parameter must be SmsParams."):
            self.sut.send_simple(None)

            self.worker_mock.execute.assert_not_called()

    def test_send_simple_Error(self):
        expected = ["123456"], "body", "sender"

        # Execute method
        params = SmsParams(*expected)
        mock = MagicMock()
        mock.return_value = '{"_links": {"self": {"href": "https:\/\/api-eu-01.twizo.com\/v1\/sms\/submit"}},' \
                            '"total_items": 1} '

        self.service_mock.parse = mock

        with self.assertRaises(TwizoDataException):
            self.sut.send_simple(params)

    def test_send_advance(self):
        expected = "body", "123456", "sender"
        expected_extra = 15, 5

        # Execute method
        params = SmsAdvanceParams(*expected)
        params.dcs = expected_extra[0]
        params.udh = expected_extra[1]

        self.sut.send_advanced(params)

        self.worker_mock.execute.assert_called_once_with(
            url="sms/submit",
            parameters=json.dumps(params.__dict__),
            request_type=RequestType.POST,
            expected_status=201
        )

        self.service_mock.parse.assert_called_once()

    def test_send_advance_Error(self):
        expected = "body", "123456", "sender"

        # Execute method
        params = SmsAdvanceParams(*expected)
        mock = MagicMock()
        mock.return_value = '{"_links": {"self": {"href": "https:\/\/api-eu-01.twizo.com\/v1\/sms\/submit"}},' \
                            '"total_items": 1} '

        self.service_mock.parse = mock

        with self.assertRaises(TwizoDataException):
            self.sut.send_advanced(params)

    def test_send_advance_EmptyParam(self):
        with self.assertRaisesRegex(TwizoParamsException, "Parameter must be SmsAdvanceParams."):
            self.sut.send_advanced(None)

        self.worker_mock.execute.assert_not_called()

    def test_get_status(self):
        expected = "message_id"
        self.sut.get_status(expected)

        self.worker_mock.execute.assert_called_once_with(
            url="sms/submit/%s" % expected,
            request_type=RequestType.GET,
            expected_status=200
        )

        self.service_mock.parse.assert_called_once()

    def test_get_delivery_report(self):
        batch_id = "151475a39e68a652014.31799847"
        model = TwizoModel()
        model._embedded = TwizoModel()
        model._embedded.messages = ""
        model.batchId = batch_id

        self.service_mock.parse = MagicMock(
            return_value=model)

        print(self.sut.get_delivery_report())

        self.worker_mock.execute.assert_has_calls([
            call(url="sms/poll",
                 request_type=RequestType.GET,
                 expected_status=200),
            call(url="sms/poll/%s" % batch_id,
                 request_type=RequestType.DELETE,
                 expected_status=204)
        ])

        self.service_mock.parse.assert_called_once()

    def test_get_delivery_report_Error(self):
        batch_id = "151475a39e68a652014.31799847"
        model = TwizoModel()
        model.batchId = batch_id

        self.service_mock.parse = MagicMock(
            return_value=model)

        result = self.sut.get_delivery_report()
        self.assertEquals(result, [])


if __name__ == '__main__':
    unittest.main()
