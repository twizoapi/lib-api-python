import unittest
from unittest.mock import MagicMock

from controllers import ApplicationController
from enums import RequestType
from service import TwizoService
from worker import Worker


class ApplicationControllerTest(unittest.TestCase):
    def test_get_verification_types(self):
        return_value = '{"key":"value"}'

        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock(return_value=return_value)
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = ApplicationController(worker_mock, service_mock)

        self.sut.get_verification_types()

        worker_mock.execute.assert_called_once_with(
            url="application/verification_types",
            request_type=RequestType.GET,
            expected_status=200
        )

        service_mock.parse.assert_called_once_with(return_value, list)

    def test_verify_credentials(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = ApplicationController(worker_mock, service_mock)

        self.sut.verify_credentials()

        worker_mock.execute.assert_called_once_with(
            url="application/verifycredentials",
            request_type=RequestType.GET,
            expected_status=200
        )

        service_mock.parse.assert_called_once()


if __name__ == '__main__':
    unittest.main()
