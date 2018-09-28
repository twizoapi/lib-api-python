import pprint
import random

from examples.api_key import api_host, api_key
from exceptions import TwizoApiException
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)
    pprint = pprint.PrettyPrinter(indent=4)

    controller = twizo.bio_voice_controller

    recipient = random.randint(100000000, 999999999)

    print("\n   create:   \n")
    result = controller.create_registration(recipient)
    pprint.pprint(vars(result))

    print("\n   Check status registration:   \n")
    result = controller.check_status_registration(result.registrationId)
    pprint.pprint(vars(result))

    # Will throw a TwizoApiException because there is no current subscription
    print("\n   Check status subscription:   \n")
    try:
        result = controller.check_status_subscription(recipient)
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)

    print("\n   Delete subscription:   \n")
    result = controller.delete_subscription(recipient)
    print("Deleted: %s" % recipient)

    print("\n   Check if it still exist:   \n")
    try:
        result = controller.check_status_subscription(recipient)
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)
