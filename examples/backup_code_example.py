import pprint
import random
import time

from examples.api_key import api_host, api_key
from exceptions import TwizoApiException
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    pprint = pprint.PrettyPrinter(indent=4)

    controller = twizo.backup_code_controller

    # make sure identifier is different each time
    identifier = random.randint(100000000, 999999999)

    print("\n   create:   \n")
    result = controller.create(identifier)
    pprint.pprint(vars(result))

    try:
        print("\n   Verify code incorrect:   \n")
        result = controller.verify(identifier, "INVALID TOKEN")
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)

    time.sleep(2)

    print("\n   Verify code correct:   \n")
    result = controller.verify(identifier, "00000000")
    pprint.pprint(vars(result))

    time.sleep(2)

    print("\n   Check remaining:   \n")
    result = controller.check_remaining(identifier)
    pprint.pprint(vars(result))

    time.sleep(2)

    print("\n   Update:   \n")
    result = controller.update(identifier)
    pprint.pprint(vars(result))

    time.sleep(2)

    print("\n   Delete:   \n")
    result = controller.delete(identifier)
    print("Deleted: %s" % identifier)

    print("\n   Check if it still exist:   \n")
    try:
        result = controller.check_remaining(identifier)
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)
