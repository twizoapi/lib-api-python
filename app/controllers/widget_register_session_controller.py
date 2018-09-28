import json

from controllers import TwizoController
from enums import RequestType
from exceptions import TwizoParamsException
from models.parameters import WidgetRegisterSessionParams
from models.result import WidgetRegisterSession


class WidgetRegisterSessionController(TwizoController):
    def create(self, params: WidgetRegisterSessionParams) -> WidgetRegisterSession:
        """
        Create a new widgetRegistrationSession and parse the result to a WidgetRegistrationSession object

        Args:
            params:
        Raises:
              TwizoParamsException
        Returns:
            WidgetRegistrationSession object
        """
        if not isinstance(params, WidgetRegisterSessionParams):
            raise TwizoParamsException("Wrong parameter type.")

        return self._service.parse(
            self._worker.execute(url="widget-register-verification/session", request_type=RequestType.POST,
                                 parameters=json.dumps(params.__dict__), expected_status=201)
        )
