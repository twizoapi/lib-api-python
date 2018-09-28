import json
import unittest
from unittest.mock import MagicMock

from controllers import WidgetSessionController
from enums import RequestType, WidgetSessionType
from exceptions import TwizoParamsException
from models.parameters import WidgetSessionParams
from service import TwizoService
from worker import Worker


class NumberLookupControllerTest(unittest.TestCase):
    def test_create(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetSessionController(worker_mock, service_mock)

        expected = "1234567890"
        # Execute method
        params = WidgetSessionParams(['sms', 'call'], [expected])
        self.sut.create(params)

        worker_mock.execute.assert_called_once_with(
            url="widget/session",
            parameters=json.dumps(params.__dict__),
            request_type=RequestType.POST,
            expected_status=201
        )

        service_mock.parse.assert_called_once()

    def test_create_EmptyParam(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetSessionController(worker_mock, service_mock)

        with self.assertRaisesRegex(TwizoParamsException, "Wrong parameter type."):
            self.sut.create(None)

    def test_get_session_status_Recipient(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetSessionController(worker_mock, service_mock)

        session_token = "1234567890"
        recipient = "0123456789987"
        # Execute method
        self.sut.get_session_status(session_token, recipient, "", WidgetSessionType.RECIPIENT)

        worker_mock.execute.assert_called_once_with(
            url="widget/session/%s?recipient=%s" % (session_token, recipient),
            request_type=RequestType.GET,
            expected_status=200
        )

        service_mock.parse.assert_called_once()

    def test_get_session_status_BackupCode(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetSessionController(worker_mock, service_mock)

        session_token = "1234567890"
        identifier = "01234566"
        # Execute method
        self.sut.get_session_status(session_token, "", identifier, WidgetSessionType.BACKUPCODE)

        worker_mock.execute.assert_called_once_with(
            url="widget/session/%s?backupCodeIdentifier=%s" % (session_token, identifier),
            request_type=RequestType.GET,
            expected_status=200
        )

        service_mock.parse.assert_called_once()

    def test_get_session_status_Both(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetSessionController(worker_mock, service_mock)

        session_token = "1234567890"
        recipient = "0123456789789"
        identifier = "0123456"
        # Execute method
        self.sut.get_session_status(session_token, recipient, identifier, WidgetSessionType.BOTH)

        worker_mock.execute.assert_called_once_with(
            url="widget/session/%s?recipient=%s&backupCodeIdentifier=%s" % (session_token, recipient, identifier),
            request_type=RequestType.GET,
            expected_status=200
        )

        service_mock.parse.assert_called_once()

    def test_get_session_status_Empty(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetSessionController(worker_mock, service_mock)

        session_token = "1234567890"
        recipient = "0123456789789"
        identifier = "0123456"
        # Execute method
        self.sut.get_session_status(session_token, recipient, identifier, None)

        worker_mock.execute.assert_not_called()

        service_mock.parse.assert_not_called()


if __name__ == '__main__':
    unittest.main()
