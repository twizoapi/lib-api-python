from typing import Any

from exceptions import TwizoException


class TwizoParamsException(TwizoException):
    def __init__(self, *args: Any) -> None:
        """
        Parameters related exception

        Args:
            *args: Error message
        """
        super().__init__(*args)
