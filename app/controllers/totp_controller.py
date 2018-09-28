from controllers import TwizoController
from enums import RequestType
from models.result import *


class TotpController(TwizoController):
    def create(self, identifier: str, issuer: str) -> Totp:
        """
        Create a new totp and parse the result to a TOTP object

        Args:
            identifier: This is a mandatory string parameter. The identifier must be a unique identifier of the
                        user, e.g. an email address. The identifier will be visible in the Twizo Authenticator app as
                        the application name.
            issuer: This is a mandatory string parameter. The issuer is the name of the site the user wants to
                        login to. The issuer will be visible to the user when he scans the TOTP with the Twizo
                        Authenticator app and shows for which website the TOTP is.

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            Totp object
        """
        return self._service.parse(
            self._worker.execute(url="totp", request_type=RequestType.POST,
                                 parameters='{"identifier": "%s", "issuer": "%s"}' % (identifier, issuer),
                                 expected_status=201)
        )

    def verify(self, identifier: str, token: str) -> TotpResponseSuccess:
        """
        When the user uses a TOTP token and entered it in your website,
        the API will verify the token with the TOTP generated for the user.

        Args:
            identifier: The identifier you used to generate the TOTP for the user.
            token: The TOTP token entered by the user and you want to verify with the generated TOTP for the user.

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            TotpResponseSuccess or TotpResponseFailed object
        """
        return self._service.parse(
            self._worker.execute(url="totp/%s?token=%s" % (identifier, token), request_type=RequestType.GET,
                                 expected_status=200)
        )

    def check_status(self, identifier: str) -> Totp:
        """
        To check the status of a TOTP

        Args:
            identifier: The identifier you used to generate the TOTP for the user.

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            Totp object
        """
        return self._service.parse(
            self._worker.execute(url="totp/%s" % identifier, request_type=RequestType.GET, expected_status=200)
        )

    def delete(self, identifier: str):
        """
        To check the status of a TOTP

        Args:
            identifier: The identifier you used to generate the TOTP for the user.

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            None
        """
        self._worker.execute(url="totp/%s" % identifier, request_type=RequestType.DELETE, expected_status=204)
