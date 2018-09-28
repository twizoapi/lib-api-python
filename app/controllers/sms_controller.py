import json
from typing import List

from controllers import TwizoController
from enums import RequestType
from exceptions import TwizoParamsException, TwizoDataException
from models.parameters import SmsParams, SmsAdvanceParams
from models.result import Sms


class SmsController(TwizoController):
    def send_simple(self, params: SmsParams) -> List[Sms]:
        """
        Create and sendSimple a new Sms and parse the result to a Sms object

        Args:
            params:
        Raises:
            TwizoParamsException
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            List of Sms
        """
        if not isinstance(params, SmsParams):
            raise TwizoParamsException("Parameter must be SmsParams.")

        result = self._service.parse(
            self._worker.execute(url="sms/submitsimple", request_type=RequestType.POST,
                                 parameters=json.dumps(params.__dict__), expected_status=201)
        )

        if hasattr(result, '_embedded'):
            return result._embedded.items
        else:
            raise TwizoDataException("No SMS objects returned.\n", result)

    def send_advanced(self, params: SmsParams) -> List[Sms]:
        """
        Create and sendSimple a new Sms and parse the result to a Sms object

        Args:
            params:
        Raises:
            TwizoParamsException
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            List of Sms
        """
        if not isinstance(params, SmsAdvanceParams):
            raise TwizoParamsException("Parameter must be SmsAdvanceParams.")

        result = self._service.parse(
            self._worker.execute(url="sms/submit", request_type=RequestType.POST,
                                 parameters=json.dumps(params.__dict__), expected_status=201)
        )

        if hasattr(result, '_embedded'):
            return result._embedded.items
        else:
            raise TwizoDataException("No SMS objects returned.\n", result)

    def get_status(self, message_id: str) -> Sms:
        """
        Get the status of a Sms and parse it to a Sms object

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            Sms Object
        """
        return self._service.parse(
            self._worker.execute(url="sms/submit/%s" % message_id, request_type=RequestType.GET, expected_status=200)
        )

    def get_delivery_report(self) -> List[Sms]:
        """
        Poll results about Sms delivery reports.

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            List of Sms
        """
        result = self._service.parse(
            self._worker.execute(url="sms/poll", request_type=RequestType.GET, expected_status=200)
        )

        if hasattr(result, '_embedded'):
            messages = result._embedded.messages
        else:
            messages = []

        batch_id = result.batchId if result.batchId is not "" else "NULL"

        self._worker.execute(url="sms/poll/%s" % batch_id, request_type=RequestType.DELETE, expected_status=204)

        return messages
