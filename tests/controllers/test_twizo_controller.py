import unittest

from controllers import TwizoController
from service import TwizoService
from worker import Worker


class TwizoControllerTest(unittest.TestCase):
    def test_get_worker(self):
        worker_mock = Worker("", "")
        service_mock = TwizoService()
        self.sut = TwizoController(worker_mock, service_mock)

        self.assertEqual(worker_mock, self.sut._worker)

    def test_set_worker(self):
        worker_mock = Worker("", "")
        service_mock = TwizoService()
        self.sut = TwizoController(worker_mock, service_mock)
        self.sut._worker = new_worker = Worker("new", "new")

        self.assertEqual(new_worker, self.sut._worker)


if __name__ == '__main__':
    unittest.main()
