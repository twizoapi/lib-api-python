from abc import ABCMeta

from enums import RequestType


class Worker(metaclass=ABCMeta):
    def __init__(self, api_key: str, api_host: str):
        """
        Args:
            api_key: API key used for authentication to the Twizo API server
            api_host: API host node
        """
        self._api_host = api_host
        self._api_key = api_key

    def execute(self, url: str, request_type: RequestType, parameters: str or None = None, expected_status=None) -> str:
        """

        Args:
            url: Parameter to specify API action
            parameters: Parameters which can be added to an API request
            request_type: Type of request
            expected_status: Expected HTTP Status of request

        Returns:
            String in JSON format with retrieved information

        Raises:
            TwizoApiException

        """
        raise NotImplementedError
