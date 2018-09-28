import pprint

from examples.api_key import api_host, api_key
from models.parameters import WidgetRegisterSessionParams
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    controller = twizo.widget_register_session_controller

    recipient = "123456789"
    params = WidgetRegisterSessionParams()
    params.recipient = recipient

    print("\n   create:   \n")
    result = controller.create(params)
    pprint.pprint(vars(result))
    print("\nsessionToken:")
    print(result.sessionToken)
