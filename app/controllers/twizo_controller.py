from abc import ABCMeta

from service import TwizoService
from worker import Worker


class TwizoController(metaclass=ABCMeta):
    def __init__(self, worker: Worker, twizo_service: TwizoService):
        """
        Args:
            worker: Worker instance to communicate with Twizo's servers
        """
        self.__worker = worker
        self._service = twizo_service

    @property
    def _worker(self) -> Worker:
        """
        Returns:
            Worker to be used as executor of commands.
        """
        return self.__worker

    @_worker.setter
    def _worker(self, worker: Worker) -> None:
        """
        Args:
            worker: set self.worker to worker
        """
        self.__worker = worker
