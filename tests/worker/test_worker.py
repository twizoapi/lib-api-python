import unittest

from enums import RequestType
from worker import Worker


class HttpClientTest(unittest.TestCase):
    def test_execute_NotImplementedError(self):
        api_host = ""
        api_key = ""
        self.sut = Worker(api_key, api_host)

        with self.assertRaises(NotImplementedError):
            self.sut.execute("", RequestType.GET, "")


if __name__ == '__main__':
    unittest.main()
