from typing import Any


class TwizoException(Exception):
    """
    Exception thrown by twizo classes.
    """

    def __init__(self, *args: Any) -> None:
        Exception.__init__(self, args)
