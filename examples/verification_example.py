import pprint

from examples.api_key import api_host, api_key
from exceptions import TwizoApiException
from models.parameters import VerificationParams
from twizo import Twizo

if __name__ == '__main__':
    twizo = Twizo(api_key=api_key,
                  api_host=api_host)

    params = VerificationParams('12345000000')
    pprint = pprint.PrettyPrinter(indent=4)

    controller = twizo.verification_controller

    print("\n   create:   \n")
    result = controller.create(params)
    pprint.pprint(vars(result))

    try:
        print("\n   Verify token incorrect:   \n")
        result = controller.verify_token(result.messageId, "invalidToken")
        pprint.pprint(vars(result))
    except TwizoApiException as ex:
        pprint.pprint(ex)

    print("\n   Verify token correct:   \n")
    result = controller.verify_token(controller.create(params).messageId, "012345")
    pprint.pprint(vars(result))

    print("\n   Get status:   \n")
    result = controller.get_status(result.messageId)
    pprint.pprint(vars(result))
