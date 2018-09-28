from typing import Any

from exceptions import TwizoException


class TwizoDataException(TwizoException):
    def __init__(self, *args: Any) -> None:
        """
        Data related exception

        Args:
            *args: Error message
        """
        super().__init__(*args)
