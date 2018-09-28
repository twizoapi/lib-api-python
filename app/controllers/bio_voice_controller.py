from controllers import TwizoController
from enums import RequestType
from models.result import BioVoice


class BioVoiceController(TwizoController):
    def create_registration(self, recipient: str) -> BioVoice:
        """
        Create a new bio voice registration and parse the result to a BioVoice object

        Args:
            recipient: Number of to be registered user
        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            BioVoice object
        """
        return self._service.parse(
            self._worker.execute(url="biovoice/registration", request_type=RequestType.POST,
                                 parameters='{"recipient": "%s"}' % recipient, expected_status=201)
        )

    def check_status_registration(self, registration_id: str) -> BioVoice:
        """
        Get bio voice registration status for the supplied registrationId
        While a registration is in progress, you cannot perform a bio voice verification yet.

        Args:
            registration_id: The registration id returned on registration creation
        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            BioVoice object
        """
        return self._service.parse(
            self._worker.execute(url="biovoice/registration/%s" % registration_id, request_type=RequestType.GET,
                                 expected_status=200)
        )

    def check_status_subscription(self, recipient: str) -> BioVoice:
        """
        To check the status of a bio voice subscription.

        Args:
            recipient: The recipient number you used for creating the bio voice registration for the user.
        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            BioVoice object
        """
        return self._service.parse(
            self._worker.execute(url="biovoice/subscription/%s" % recipient, request_type=RequestType.GET,
                                 expected_status=200)
        )

    def delete_subscription(self, recipient: str) -> None:
        """
        To delete the bio voice subscription of a user.
        The user will then not be able to use the bio voice verification anymore.

        Args:
            recipient: The recipient number you used for creating the bio voice registration for the user.
        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            BioVoice object
        """
        self._worker.execute(url="biovoice/subscription/%s" % recipient, request_type=RequestType.DELETE,
                             expected_status=204)
