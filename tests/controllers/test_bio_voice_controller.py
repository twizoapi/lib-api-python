import unittest
from unittest.mock import MagicMock

from controllers import BioVoiceController
from enums import RequestType
from service import TwizoService
from worker import Worker


class BackupCodeControllerTest(unittest.TestCase):
    def setUp(self):
        self.worker_mock = Worker("", "")
        self.worker_mock.execute = MagicMock()
        self.service_mock = TwizoService()
        self.service_mock.parse = MagicMock()

        self.sut = BioVoiceController(self.worker_mock, self.service_mock)

    def test_create(self):
        recipient = "12345678"
        self.sut.create_registration(recipient)
        self.worker_mock.execute.assert_called_once_with(
            url="biovoice/registration",
            request_type=RequestType.POST,
            parameters='{"recipient": "%s"}' % recipient,
            expected_status=201
        )
        self.service_mock.parse.assert_called_once()

    def test_check_status_registration(self):
        registration_id = "12345678"
        self.sut.check_status_registration(registration_id)
        self.worker_mock.execute.assert_called_once_with(
            url="biovoice/registration/%s" % registration_id,
            request_type=RequestType.GET,
            expected_status=200
        )
        self.service_mock.parse.assert_called_once()

    def test_check_status_subscription(self):
        recipient = "12345678"
        self.sut.check_status_subscription(recipient)
        self.worker_mock.execute.assert_called_once_with(
            url="biovoice/subscription/%s" % recipient,
            request_type=RequestType.GET,
            expected_status=200
        )
        self.service_mock.parse.assert_called_once()

    def test_delete_subscription(self):
        recipient = "12345678"
        self.sut.delete_subscription(recipient)
        self.worker_mock.execute.assert_called_once_with(
            url="biovoice/subscription/%s" % recipient,
            request_type=RequestType.DELETE,
            expected_status=204
        )


if __name__ == '__main__':
    unittest.main()
