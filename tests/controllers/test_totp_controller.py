import unittest
from unittest.mock import MagicMock

from controllers import TotpController
from enums import RequestType
from service import TwizoService
from worker import Worker


class NumberLookupControllerTest(unittest.TestCase):
    def setUp(self):
        self.worker_mock = Worker("", "")
        self.worker_mock.execute = MagicMock()
        self.service_mock = TwizoService()
        self.service_mock.parse = MagicMock()

        self.sut = TotpController(self.worker_mock, self.service_mock)

    def test_create(self):
        identifier = "123456"
        issuer = "TEST"
        self.sut.create(identifier, issuer)

        self.worker_mock.execute.assert_called_once_with(
            url="totp",
            request_type=RequestType.POST,
            parameters='{"identifier": "%s", "issuer": "%s"}' % (identifier, issuer),
            expected_status=201
        )

        self.service_mock.parse.assert_called_once()

    def test_verify(self):
        identifier = "123456"
        token = "TEST"

        # Execute method
        self.sut.verify(identifier, token)

        # Check if worker calls are done
        self.worker_mock.execute.assert_called_once_with(
            url="totp/%s?token=%s" % (identifier, token),
            request_type=RequestType.GET,
            expected_status=200
        )

        self.service_mock.parse.assert_called_once()

    def test_check_status(self):
        identifier = "123456"
        self.sut.check_status(identifier)

        # Check if worker calls are done
        self.worker_mock.execute.assert_called_once_with(
            url="totp/%s" % identifier,
            request_type=RequestType.GET,
            expected_status=200
        )

        self.service_mock.parse.assert_called_once()

    def test_delete(self):
        identifier = "123456"
        self.sut.delete(identifier)

        # Check if worker calls are done
        self.worker_mock.execute.assert_called_once_with(
            url="totp/%s" % identifier,
            request_type=RequestType.DELETE,
            expected_status=204
        )


if __name__ == '__main__':
    unittest.main()
