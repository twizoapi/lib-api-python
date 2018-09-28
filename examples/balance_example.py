import pprint

from examples.api_key import api_key, api_host
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    controller = twizo.balance_controller
    pprint = pprint.PrettyPrinter(indent=4)

    result = controller.get_credit_balance()
    pprint.pprint(vars(result))
