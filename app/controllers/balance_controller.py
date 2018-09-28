from controllers import TwizoController
from enums import RequestType
from models.result import Balance


class BalanceController(TwizoController):
    def get_credit_balance(self) -> Balance:
        """
        Get Balance of the user and parse it to a Balance object

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            Balance object
        """
        return self._service.parse(
            self._worker.execute(url="wallet/getbalance", request_type=RequestType.GET, expected_status=200)
        )
