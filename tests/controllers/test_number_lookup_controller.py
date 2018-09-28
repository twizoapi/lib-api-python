import json
import unittest
from unittest.mock import MagicMock, call

from controllers import NumberLookupController
from enums import RequestType
from exceptions import TwizoParamsException, TwizoDataException
from models import TwizoModel
from models.parameters import NumberLookupParams
from service import TwizoService
from worker import Worker


class NumberLookupControllerTest(unittest.TestCase):
    def setUp(self):
        self.worker_mock = Worker("", "")
        self.worker_mock.execute = MagicMock()
        self.service_mock = TwizoService()
        self.service_mock.parse = MagicMock()

        self.sut = NumberLookupController(self.worker_mock, self.service_mock)

    def test_create(self):
        params = NumberLookupParams([])
        self.sut.create(params)

        self.worker_mock.execute.assert_called_once_with(
            url="numberlookup/submit",
            parameters=json.dumps(params.__dict__),
            request_type=RequestType.POST,
            expected_status=201
        )

        self.service_mock.parse.assert_called_once()

    def test_create_EmptyParam(self):
        with self.assertRaisesRegex(TwizoParamsException, "Wrong parameter type."):
            self.sut.create(None)

        self.worker_mock.execute.assert_not_called()

    def test_get_status(self):
        expected = "asia-01-1.21845.nrl5a39e568a05af1.86312955"

        # Execute method
        self.sut.get_status(expected)

        # Check if worker calls are done
        self.worker_mock.execute.assert_called_once_with(
            url="numberlookup/submit/%s" % expected,
            request_type=RequestType.GET,
            expected_status=200
        )
        self.service_mock.parse.assert_called_once()

    def test_get_poll_result(self):
        batch_id = "151475a39e68a652014.31799847"
        model = TwizoModel()
        model._embedded = TwizoModel()
        model._embedded.messages = ""
        model.batchId = batch_id

        self.service_mock.parse = MagicMock(
            return_value=model)

        # Execute method
        self.sut.get_poll_result()

        # Check if worker calls are done
        self.worker_mock.execute.assert_has_calls([
            call(url="numberlookup/poll",
                 request_type=RequestType.GET,
                 expected_status=200),
            call(url=("numberlookup/poll/%s" % batch_id),
                 request_type=RequestType.DELETE,
                 expected_status=204)
        ])
        self.service_mock.parse.assert_called_once()

    def test_get_poll_result_Error(self):
        mock = MagicMock()
        mock.return_value = '{"_links": {"self": {"href": "https:\/\/api-eu-01.twizo.com\/v1\/sms\/submit"}},' \
                            '"total_items": 1} '

        self.service_mock.parse = mock

        with self.assertRaises(TwizoDataException):
            self.sut.get_poll_result()


if __name__ == '__main__':
    unittest.main()
