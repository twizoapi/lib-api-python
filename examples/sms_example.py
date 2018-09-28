import pprint

from examples.api_key import api_key, api_host
from models.parameters import SmsAdvanceParams, SmsParams
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    params = SmsParams(['12345600000', '432543254'], "A SMS Message", '01023456789')
    params.resultType = 2
    pprint = pprint.PrettyPrinter(indent=4)

    controller = twizo.sms_controller
    result = controller.send_simple(params)
    for sms in result:
        pprint.pprint(vars(sms))

    print("\n   One recipient:   \n")

    params = SmsParams(['12345600000'], "A SMS Message", '01023456789')

    result = controller.send_simple(params)

    pprint.pprint(vars(result[0]))

    print("\n   Advanced sms:   \n")

    params = SmsAdvanceParams(params.recipients, params.body, params.sender)

    params.udh = "0A"
    params.dcs = 2
    result = controller.send_advanced(params)

    pprint.pprint(vars(result[0]))

    print("\n   get sms status:   \n")

    result = controller.get_status(result[0].messageId)
    pprint.pprint(vars(result))

    print("\n   get delivery report:   \n")

    result = controller.get_delivery_report()
    for sms in result:
        pprint.pprint(vars(sms))
