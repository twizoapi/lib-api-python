from exceptions import TwizoException


class TwizoJsonException(TwizoException):
    def __init__(self, message) -> None:
        """
        Json parsed is invalid.

        Args:
            message:
        """
        self.text = message
        super().__init__("Invalid JSON inputted. Message: %s" % message)
