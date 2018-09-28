from exceptions import TwizoException


class TwizoApiException(TwizoException):
    def __init__(self, status_code, expected_status_code, text) -> None:
        """
        Args:
            status_code: Status code returned by api client
            expected_status_code: Status code expected by the request
            text: Error text given by API connection client

        """
        super().__init__(
            "The server responded with status code: %d, expected: %d. Message: %s" %
            (status_code, expected_status_code, text)
        )
