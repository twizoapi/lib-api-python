from concurrent.futures import ThreadPoolExecutor

import requests
from requests import Response
from requests.auth import HTTPBasicAuth

from enums import RequestType
from exceptions import TwizoApiException, TwizoParamsException
from worker import Worker


class HttpClient(Worker):
    def __init__(self, api_key: str, api_host: str):
        super().__init__(api_key, api_host)
        self.pool = ThreadPoolExecutor()

    def execute(self, url: str, request_type: RequestType, parameters: str or None = None, expected_status=None) -> str:
        return self.pool.submit(HttpClient.__do_call, self._api_key, self._api_host, url, parameters,
                                request_type, expected_status).result()

    @staticmethod
    def __do_call(api_key, api_host, url: str, parameters: str or None, request_type: RequestType,
                  expected_status) -> str:
        """
        Args:
            api_key: API key used for authentication to the Twizo API server
            api_host: API host node
            url: Parameter to specify API action
            parameters: Parameters which can be added to an API request
            request_type: Type of request
            expected_status: Status code expected by the request

        Returns:
            String in JSON format with retrieved information

        Raises:
            TwizoApiException

        """
        url = "https://" + api_host + "/" + url

        # Make a basic auth base64 hash object
        auth = HTTPBasicAuth("twizo", api_key)

        response = HttpClient.__switch_request_type(request_type, url, auth, parameters)

        if response.status_code == expected_status:
            return response.text
        else:
            raise TwizoApiException(response.status_code, expected_status, response.text)

    @staticmethod
    def __switch_request_type(request_type: RequestType, url: str, auth: HTTPBasicAuth, parameters: str) -> Response:
        """
        Args:
            request_type: Type of request
            url: Parameter to specify API action
            auth: HTTPBasicAuth base64 hash of credentials
            parameters: Parameters which can be added to an API request

        Returns:
            Response of http response

        """
        import platform
        import pkg_resources

        # Set user agent
        version = pkg_resources.require('twizo-lib-python3')[0].version  # Get version from setup file
        user_agent = "{}/{} {}/{}/{}/{}".format("twizo-lib-python3", version, platform.python_implementation(),
                                                platform.python_version(),
                                                platform.machine(), platform.system())

        if request_type == RequestType.PUT:
            response = requests.put(url=url,
                                    auth=auth,
                                    data=parameters,
                                    headers={
                                        'User-Agent': user_agent,
                                        'Accept': 'application/json',
                                        'Content-type': 'application/json'}
                                    )

        elif request_type == RequestType.GET:
            response = requests.get(url=url,
                                    auth=auth,
                                    data=parameters,
                                    headers={
                                        'User-Agent': user_agent,
                                        'Content-type': 'application/json'}
                                    )

        elif request_type == RequestType.POST:
            response = requests.post(url=url,
                                     data=parameters,
                                     auth=auth,
                                     headers={
                                         'User-Agent': user_agent,
                                         'Accept': 'application/json',
                                         'Content-type': 'application/json'}
                                     )

        elif request_type == RequestType.DELETE:
            response = requests.delete(url=url,
                                       auth=auth,
                                       data=parameters,
                                       headers={
                                           'User-Agent': user_agent,
                                           'Content-type': 'application/json'}
                                       )
        else:
            raise TwizoParamsException("No RequestType specified.")
        return response
