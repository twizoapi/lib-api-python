import pprint

from enums import WidgetSessionType
from examples.api_key import api_host, api_key
from models.parameters import WidgetSessionParams
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    controller = twizo.widget_session_controller

    recipient = "123456789"
    params = WidgetSessionParams(["sms"], recipient)

    print("\n   create:   \n")
    result = controller.create(params)
    pprint.pprint(vars(result))
    print("\nsessionToken:")
    print(result.sessionToken)

    print("\n   Get status:   \n")
    result = controller.get_session_status(result.sessionToken, recipient, None, WidgetSessionType.RECIPIENT)
    pprint.pprint(vars(result))
