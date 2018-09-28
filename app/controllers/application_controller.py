from typing import List

from controllers import TwizoController
from enums import RequestType
from models.result import VerifyCredentials


class ApplicationController(TwizoController):
    def get_verification_types(self) -> List:
        """
        Get allowed types for a specific API key

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            List of allowed types

        """
        return self._service.parse(
            self._worker.execute(url="application/verification_types", request_type=RequestType.GET,
                                 expected_status=200),
            list
        )

    def verify_credentials(self) -> VerifyCredentials:
        """
        Get details about the entered API key

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            VerifyCredentials object containing information about the key

        """
        return self._service.parse(
            self._worker.execute(url="application/verifycredentials", request_type=RequestType.GET, expected_status=200)
        )
