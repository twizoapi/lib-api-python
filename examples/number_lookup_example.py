import pprint

from examples.api_key import api_key, api_host
from models.parameters import NumberLookupParams
from models.result import NumberLookup
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    params = NumberLookupParams(numbers=["31683802490"])

    params.tag = "Python"

    controller = twizo.number_lookup_controller
    pprint = pprint.PrettyPrinter(indent=4)

    result = controller.create(params)
    pprint.pprint((result[0]))

    message_id = result[0].messageId
    print("message_id - ", message_id)

    status_result = NumberLookup()
    count = 0  # set a max amount of tries
    while not status_result.status == "delivered" and count < 20:
        status_result = controller.get_status(message_id)
        print(status_result.status)
        count += 1

    poll_result = controller.get_poll_result()
    if len(poll_result) > 0:
        pprint.pprint(vars(poll_result[0]))
