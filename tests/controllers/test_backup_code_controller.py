import unittest
from unittest.mock import MagicMock

from controllers import BackupCodeController
from enums import RequestType
from service import TwizoService
from worker import Worker


class BackupCodeControllerTest(unittest.TestCase):
    def setUp(self):
        self.worker_mock = Worker("", "")
        self.worker_mock.execute = MagicMock()
        self.service_mock = TwizoService()
        self.service_mock.parse = MagicMock()

        self.sut = BackupCodeController(self.worker_mock, self.service_mock)

    def test_create(self):
        identifier = "identifier"
        self.sut.create(identifier)
        self.worker_mock.execute.assert_called_with(
            url="backupcode",
            request_type=RequestType.POST,
            parameters='{"identifier":"%s"}' % identifier,
            expected_status=201
        )

    def test_verify(self):
        identifier = "identifier"
        token = "token"
        self.sut.verify(identifier, token)
        self.worker_mock.execute.assert_called_with(
            url="backupcode/%s?token=%s" % (identifier, token),
            request_type=RequestType.GET,
            expected_status=200
        )

    def test_check_remaining(self):
        identifier = "identifier"
        self.sut.check_remaining(identifier)
        self.worker_mock.execute.assert_called_with(
            url="backupcode/%s" % identifier,
            request_type=RequestType.GET,
            expected_status=200
        )

    def test_update(self):
        identifier = "identifier"
        self.sut.update(identifier)
        self.worker_mock.execute.assert_called_with(
            url="backupcode/%s" % identifier,
            request_type=RequestType.PUT,
            parameters='{"identifier":"%s"}' % identifier,
            expected_status=200
        )

    def test_delete(self):
        identifier = "identifier"
        self.sut.delete(identifier)
        self.worker_mock.execute.assert_called_with(
            url="backupcode/%s" % identifier,
            request_type=RequestType.DELETE,
            expected_status=204
        )


if __name__ == '__main__':
    unittest.main()
