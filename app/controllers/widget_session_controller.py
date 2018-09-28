import json

from controllers import TwizoController
from enums import RequestType, WidgetSessionType
from exceptions import TwizoParamsException
from models.parameters import WidgetSessionParams
from models.result import WidgetSession


class WidgetSessionController(TwizoController):
    def create(self, params: WidgetSessionParams) -> WidgetSession:
        """
        Create a new widgetSession and parse the result to a WidgetSession object

        Args:
            params (WidgetSessionParams): WidgetSessionParams object to add parameters to request

        Raises:
            TwizoParamsException
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            WidgetSession object
        """
        if not isinstance(params, WidgetSessionParams):
            raise TwizoParamsException("Wrong parameter type.")

        return self._service.parse(
            self._worker.execute(url="widget/session", request_type=RequestType.POST,
                                 parameters=json.dumps(params.__dict__), expected_status=201)
        )

    def get_session_status(self, session_token: str, recipient: str, identifier: str,
                           widget_session_type: WidgetSessionType) -> WidgetSession:
        """
        Create a new widgetSession and parse the result to a WidgetSession object

        Args:
            session_token: identifier of the session
            recipient: phone number specified for the session
            identifier: backup code identifier
            widget_session_type:

        Raises:
            TwizoDataException
            TwizoJsonException
            TwizoApiException

        Returns:
            WidgetSession object
        """
        if widget_session_type == WidgetSessionType.RECIPIENT:
            url = "widget/session/%s?recipient=%s" % (session_token, recipient)
        elif widget_session_type == WidgetSessionType.BACKUPCODE:
            url = "widget/session/%s?backupCodeIdentifier=%s" % (session_token, identifier)
        elif widget_session_type == WidgetSessionType.BOTH:
            url = "widget/session/%s?recipient=%s&backupCodeIdentifier=%s" % (session_token, recipient, identifier)
        else:
            return WidgetSession()

        return self._service.parse(
            self._worker.execute(url=url, request_type=RequestType.GET, expected_status=200)
        )
