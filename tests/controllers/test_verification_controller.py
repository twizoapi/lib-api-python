import json
import unittest
from unittest.mock import MagicMock

from controllers import VerificationController
from enums import RequestType
from exceptions import TwizoParamsException
from models.parameters import VerificationParams
from service import TwizoService
from worker import Worker


class VerificationControllerTest(unittest.TestCase):
    def setUp(self):
        self.worker_mock = Worker("", "")
        self.worker_mock.execute = MagicMock()
        self.service_mock = TwizoService()
        self.service_mock.parse = MagicMock()

        self.sut = VerificationController(self.worker_mock, self.service_mock)

    def test_create_verification(self):
        params = VerificationParams('123456789')
        self.sut.create(params)

        self.worker_mock.execute.assert_called_once_with(
            url="verification/submit",
            request_type=RequestType.POST,
            parameters=json.dumps(params.__dict__),
            expected_status=201
        )

        self.service_mock.parse.assert_called_once()

    def test_create_EmptyParam(self):
        with self.assertRaisesRegex(TwizoParamsException, "Wrong parameter type."):
            self.sut.create(None)

    def test_verify_token(self):
        message_id = "123456"
        token = "012345"
        self.sut.verify_token(message_id, token)

        self.worker_mock.execute.assert_called_once_with(
            url="verification/submit/%s?token=%s" % (message_id, token),
            request_type=RequestType.GET,
            expected_status=200
        )

        self.service_mock.parse.assert_called_once()

    def test_get_status(self):
        message_id = "12345"
        self.sut.get_status(message_id)

        self.worker_mock.execute.assert_called_once_with(
            url="verification/submit/%s" % message_id,
            request_type=RequestType.GET,
            expected_status=200
        )

        self.service_mock.parse.assert_called_once()


if __name__ == '__main__':
    unittest.main()
