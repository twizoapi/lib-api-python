import json
from typing import List

from controllers import TwizoController
from enums import RequestType
from exceptions import TwizoParamsException, TwizoDataException
from models.parameters import NumberLookupParams
from models.result import NumberLookup


class NumberLookupController(TwizoController):
    def create(self, params: NumberLookupParams) -> List[NumberLookup]:
        """
        Create a new NumberLookup and parse the results to a NumberLookup array

        Args:
            params:
        Raises:
            TwizoParamsException
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            List of NumberLookups
        """
        if not isinstance(params, NumberLookupParams):
            raise TwizoParamsException("Wrong parameter type.")

        return self._service.parse(
            self._worker.execute(url="numberlookup/submit", request_type=RequestType.POST,
                                 parameters=json.dumps(params.__dict__), expected_status=201)
        )._embedded.items

    def get_status(self, message_id: str) -> NumberLookup:
        """
        Get the current status of a numberLookup by using it's messageId

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Args:
            message_id: id of the number lookup
        Returns:
            Found NumberLookup instance
        """

        return self._service.parse(
            self._worker.execute(url="numberlookup/submit/%s" % message_id, request_type=RequestType.GET,
                                 expected_status=200)
        )

    def get_poll_result(self) -> List[NumberLookup]:
        """
        Poll results about Numberlookup delivery reports.

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException
        Returns:
            List of NumberLookup results
        """

        result = self._service.parse(
            self._worker.execute(url="numberlookup/poll", request_type=RequestType.GET, expected_status=200)
        )

        if hasattr(result, '_embedded'):
            messages = result._embedded.messages
        else:
            raise TwizoDataException("No NumberLookup objects returned.")

        batch_id = result.batchId if result.batchId is not "" else "NULL"

        # Delete the delivery reports by using the batchId
        self._worker.execute(url="numberlookup/poll/%s" % batch_id, request_type=RequestType.DELETE,
                             expected_status=204)

        return messages
