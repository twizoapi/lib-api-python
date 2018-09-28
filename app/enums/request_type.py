from enum import Enum, unique


@unique
class RequestType(Enum):
    """
        HTTP Request type enum.
    """
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
