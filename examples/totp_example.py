import pprint
import random

from examples.api_key import api_host, api_key
from exceptions import TwizoApiException
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    pprint = pprint.PrettyPrinter(indent=4)

    controller = twizo.totp_controller

    print("\n   create:   \n")
    identifier = random.randint(100000, 999999)
    result = controller.create(identifier, "Twizo")
    pprint.pprint(vars(result))

    try:
        print("\n   Verify code incorrect:   \n")
        result = controller.verify(identifier, "INVALID TOKEN")
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)

    print("\n   Check status:   \n")
    result = controller.check_status(identifier)
    pprint.pprint(vars(result))

    print("\n   Delete:   \n")
    result = controller.delete(identifier)
    print("Deleted: %s" % identifier)

    print("\n   Check if it still exist:   \n")
    try:
        result = controller.check_status(identifier)
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)
