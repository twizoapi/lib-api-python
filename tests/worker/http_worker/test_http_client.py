import unittest
from unittest.mock import patch, Mock

from requests.auth import HTTPBasicAuth

from enums import RequestType
from exceptions import TwizoApiException, TwizoParamsException
from worker import HttpClient


class HttpClientTest(unittest.TestCase):
    def setUp(self):
        self.api_host = ""
        self.api_key = ""
        self.sut = HttpClient(self.api_key, self.api_host)
        # Used for generating the user agent.
        import platform
        import pkg_resources  # part of setuptools

        version = pkg_resources.require('twizo-lib-python3')[0].version

        self.user_agent = '{}/{} {}/{}/{}/{}'.format("twizo-lib-python3", version, platform.python_implementation(),
                                                     platform.python_version(),
                                                     platform.machine(), platform.system())

    def test_execute_PUT(self):
        with patch('worker.http_worker.http_client.requests', name='mock_requests') as mock_requests:
            mock_requests.put.return_value = mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = 'response'

            self.sut.execute("url", RequestType.PUT, None, 200)

            mock_requests.put.assert_called_once_with(url='https:/%s//url' % self.api_host,
                                                      data=None,
                                                      auth=HTTPBasicAuth("twizo", self.api_key),
                                                      headers={'Accept': 'application/json',
                                                               'Content-type': 'application/json',
                                                               'User-Agent': self.user_agent}
                                                      )

    def test_execute_GET(self):
        with patch('worker.http_worker.http_client.requests', name='mock_requests') as mock_requests:
            mock_requests.get.return_value = mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = 'response'

            self.sut.execute("url", RequestType.GET, None, 200)

            mock_requests.get.assert_called_once_with(url='https:/%s//url' % self.api_host,
                                                      data=None,
                                                      auth=HTTPBasicAuth("twizo", self.api_key),
                                                      headers={'User-Agent': self.user_agent}
                                                      )

    def test_execute_POST(self):
        with patch('worker.http_worker.http_client.requests', name='mock_requests') as mock_requests:
            mock_requests.post.return_value = mock_response = Mock()
            mock_response.status_code = 200
            mock_response.text = 'response'

            self.sut.execute("url", RequestType.POST, None, 200)

            mock_requests.post.assert_called_once_with(url='https:/%s//url' % self.api_host,
                                                       data=None,
                                                       auth=HTTPBasicAuth("twizo", self.api_key),
                                                       headers={'Accept': 'application/json',
                                                                'Content-type': 'application/json',
                                                                'User-Agent': self.user_agent}
                                                       )

    def test_execute_DELETE(self):
        with patch('worker.http_worker.http_client.requests', name='mock_requests') as mock_requests:
            mock_requests.delete.return_value = mock_response = Mock()
            mock_response.status_code = 204
            mock_response.text = 'response'

            response = self.sut.execute("url", RequestType.DELETE, None, 204)

            mock_requests.delete.assert_called_once_with(url='https:/%s//url' % self.api_host,
                                                         data=None,
                                                         auth=HTTPBasicAuth("twizo", self.api_key),
                                                         headers={'User-Agent': self.user_agent}
                                                         )
            self.assertEqual('response', response)

    def test_execute_DELETE_InvalidStatusCode(self):
        with patch('worker.http_worker.http_client.requests', name='mock_requests') as mock_requests:
            mock_requests.delete.return_value = mock_response = Mock()
            # Error status code
            mock_response.status_code = 404
            mock_response.text = 'response'

            with self.assertRaisesRegex(TwizoApiException,
                                        "The server responded with status code: %d, expected: %d. Message: %s" % (
                                                mock_response.status_code, 204, mock_response.text)):
                self.sut.execute("url", RequestType.DELETE, None, 204)

            mock_requests.delete.assert_called_once_with(url='https:/%s//url' % self.api_host,
                                                         data=None,
                                                         auth=HTTPBasicAuth("twizo", self.api_key),
                                                         headers={'User-Agent': self.user_agent}
                                                         )

    def test_execute_NoRequestType(self):
        with self.assertRaisesRegex(TwizoParamsException, "No RequestType specified."):
            self.sut.execute("url", None, None, 200)


if __name__ == '__main__':
    unittest.main()
