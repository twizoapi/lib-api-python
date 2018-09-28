from controllers import TwizoController
from enums import RequestType
from models.result import BackupCode


class BackupCodeController(TwizoController):
    def create(self, identifier: str) -> BackupCode:
        """
        Create new backup codes and parse them to a BackupCode object

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Args:
            identifier (str): Unique identifier to the user

        Returns:
            BackupCode object with backup codes

        """
        return self._service.parse(
            self._worker.execute(url="backupcode", request_type=RequestType.POST,
                                 parameters='{"identifier":"%s"}' % identifier, expected_status=201)
        )

    def verify(self, identifier: str, token: str) -> BackupCode:
        """
        Get the remaining backup codes of a user

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Args:
            identifier (str): Unique identifier to the user
            token (str): Backup code to be verified

        Returns:
            BackupCode object with result of the verification

        """
        return self._service.parse(
            self._worker.execute(url="backupcode/%s?token=%s" % (identifier, token), request_type=RequestType.GET,
                                 expected_status=200)
        )

    def check_remaining(self, identifier: str) -> BackupCode:
        """
        Get the remaining backup codes of a user

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Args:
            identifier (str): Unique identifier to the user

        Returns:
            BackupCode object with amount of codes left
        """
        return self._service.parse(
            self._worker.execute(url="backupcode/%s" % identifier, request_type=RequestType.GET, expected_status=200)
        )

    def update(self, identifier: str) -> BackupCode:
        """
        Update the backup codes of the user and parse the new ones to a BackupCode object

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Args:
            identifier (str): Unique identifier to the user

        Returns:
            BackupCode object with new backup codes
        """
        return self._service.parse(
            self._worker.execute(url="backupcode/%s" % identifier, request_type=RequestType.PUT,
                                 parameters='{"identifier":"%s"}' % identifier, expected_status=200)
        )

    def delete(self, identifier: str) -> None:
        """
        Delete all existing backup codes of a user and parse the result to a BackupCode object

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Args:
            identifier (str): Unique identifier to the user

        Returns:
            None
        """
        self._worker.execute(url="backupcode/%s" % identifier, request_type=RequestType.DELETE, expected_status=204)
