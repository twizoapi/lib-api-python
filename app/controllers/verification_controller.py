import json

from controllers import TwizoController
from enums import RequestType
from exceptions import TwizoParamsException
from models.parameters import VerificationParams
from models.result import Verification


class VerificationController(TwizoController):
    def create(self, params: VerificationParams) -> Verification:
        """
        Create and send a new verification and parse the result to a Verification object

        Args:
            params (VerificationParams): Verification Params
        Raises:
            TwizoParamsException
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            Verification object
        """
        if not isinstance(params, VerificationParams):
            raise TwizoParamsException("Wrong parameter type.")

        return self._service.parse(
            self._worker.execute(url="verification/submit", request_type=RequestType.POST,
                                 parameters=json.dumps(params.__dict__), expected_status=201)
        )

    def verify_token(self, message_id: str, token: str) -> Verification:
        """
        Verify a received token and parse the result to a Verification object

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Args:
            message_id (str):  Id of the received token message
            token (str): Token which has to get verified

        Returns:
            Verification object with result of Verification

        """
        return self._service.parse(
            self._worker.execute(url="verification/submit/%s?token=%s" % (message_id, token),
                                 request_type=RequestType.GET, expected_status=200)
        )

    def get_status(self, message_id: str) -> Verification:
        """
        Get the status of a verification

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            Verification object with status of Verification

        """
        return self._service.parse(
            self._worker.execute(url="verification/submit/%s" % message_id, request_type=RequestType.GET,
                                 expected_status=200)
        )
