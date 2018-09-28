import json
import unittest
from unittest.mock import MagicMock

from controllers import WidgetRegisterSessionController
from enums import RequestType
from exceptions import TwizoParamsException
from models.parameters import WidgetRegisterSessionParams
from service import TwizoService
from worker import Worker


class NumberLookupControllerTest(unittest.TestCase):
    def test_create(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = WidgetRegisterSessionController(worker_mock, service_mock)

        expected = "1234567890"
        # Execute method
        params = WidgetRegisterSessionParams()
        params.recipient = expected
        self.sut.create(params)

        worker_mock.execute.assert_called_once_with(
            url="widget-register-verification/session",
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

        self.sut = WidgetRegisterSessionController(worker_mock, service_mock)

        with self.assertRaisesRegex(TwizoParamsException, "Wrong parameter type."):
            self.sut.create(None)

if __name__ == '__main__':
    unittest.main()
