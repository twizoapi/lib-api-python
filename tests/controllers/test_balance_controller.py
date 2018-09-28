import unittest
from unittest.mock import MagicMock

from controllers import BalanceController
from enums import RequestType
from service import TwizoService
from worker import Worker


class BalanceControllerTest(unittest.TestCase):
    def test_get_credit_balance(self):
        worker_mock = Worker("", "")
        worker_mock.execute = MagicMock()
        service_mock = TwizoService()
        service_mock.parse = MagicMock()

        self.sut = BalanceController(worker_mock, service_mock)

        self.sut.get_credit_balance()

        worker_mock.execute.assert_called_once_with(
            url="wallet/getbalance",
            request_type=RequestType.GET,
            expected_status=200
        )

        service_mock.parse.assert_called_once()


if __name__ == '__main__':
    unittest.main()
