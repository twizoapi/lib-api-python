import unittest

from exceptions import TwizoDataException, TwizoJsonException
from models import *
from models.result import *
from service import TwizoService


class TwizoServiceTest(unittest.TestCase):
    def setUp(self):
        self.sut = TwizoService()

    def test_parse_set_object_type(self):
        data = '{"_links":{"self":{"href":"url"}},"_embedded":{' \
               '"items":[]},"total_items":1}'
        self.sut.parse(data, str)

        self.assertEqual(self.sut.object_type, str)

    def test_parse_empty_data(self):
        data = ''
        with self.assertRaisesRegex(TwizoDataException, "Twizo didn't collect any data. Unexpected please try again."):
            self.sut.parse(data)

    def test_parse_None_data(self):
        data = None
        with self.assertRaisesRegex(TwizoDataException, "Twizo didn't collect any data. Unexpected please try again."):
            self.sut.parse(data)

    def test_parse_incorrect_data(self):
        data = '{"incorrect json": 1337'
        with self.assertRaises(TwizoJsonException):
            self.sut.parse(data)

    def test_parse_TwizoModel(self):
        data = '{"_links":{"self":{"href":"url"}},"_embedded":{' \
               '"items":[]},"total_items":1}'
        result = self.sut.parse(data)

        self.assertEqual(type(result), TwizoModel)
        self.assertEqual(type(result._embedded), TwizoModel)

    def test_get_Sms(self):
        data = '{"applicationTag":"Python","body":"BODY OF A SMS","callbackUrl":null,' \
               '"createdDateTime":"2018-01-05T01:58:00+00:00","dcs":3,' \
               '"messageId":"asia-01-1.17039.sms5a4edba8556cc7.60175063","networkCode":null,"pid":null,' \
               '"reasonCode":null,"recipient":"123456789","resultTimestamp":null,"resultType":0,' \
               '"salesPrice":null,"salesPriceCurrencyCode":null,"scheduledDelivery":null,' \
               '"sender":"SENDER","senderNpi":1,"senderTon":2,"status":"no status","statusCode":0,' \
               '"tag":null,"udh":"A0","validity":259200,"validUntilDateTime":"2018-01-08T01:58:00+00:00",' \
               '"_links":{"self":{"href":"https:\/\/api-asia-01.twizo.com\/sms\/submit\/asia-01-1.17039' \
               '.sms5a4edba8556cc7.60175063"}}}'
        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), Sms)

    def test_get_NumberLookup(self):
        data = '{"applicationTag":"Default-application","callbackUrl":null,' \
               '"countryCode":null,"createdDateTime":"2017-12-20T04:22:00+00:00","imsi":null,' \
               '"isPorted":"Unknown","isRoaming":"Unknown",' \
               '"messageId":"messageId","msc":null,"networkCode":null,' \
               '"number":"12345600000","operator":null,"reasonCode":null, ' \
               '"resultTimestamp":null,"resultType":0,"salesPrice":null,"salesPriceCurrencyCode":null,' \
               '"status":"no status","statusCode":0,"tag":"Python","validity":259200,' \
               '"validUntilDateTime":"2017-12-23T04:22:00+00:00","_links":{"self":{' \
               '"href":"https:\/\/api-asia-01.twizo.com\/numberlookup\/submit\/asia-01-1.21845' \
               '.nrl5a39e568a05af1.86312955"}}}'

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), NumberLookup)

    def test_get_Balance(self):
        data = '{"credit": 0, "currencyCode": "", "freeVerifications": 0, "wallet": ""}'

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), Balance)

    def test_get_VerifyCredentials(self):
        data = '{"applicationTag":"Python","isTestKey":true}'

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), VerifyCredentials)

    def test_get_VerificationTypes_list(self):
        data = '{"0": "sms","1": "call","2": "backupcode"}'

        result = self.sut.parse(data, list)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), list)
        self.assertEqual(["sms", "call", "backupcode"], result)

    def test_get_Verification(self):
        data = '{"applicationTag":"Python","bodyTemplate":null,"createdDateTime":"2018-01-05T06:42:06+00:00",' \
               '"dcs":null,"issuer":"","language":null,"messageId":"messageId",' \
               '"reasonCode":null,"recipient":"0123456789","salesPrice":null,"salesPriceCurrencyCode":null,' \
               '"sender":null,"senderNpi":null,"senderTon":null,"sessionId":"dfd31088-7dd0-4ce8-b806-23d1a50277a3",' \
               '"status":"no status","statusCode":0,"tag":null,"tokenLength":null,"tokenType":null,"type":"sms",' \
               '"validity":null,"validUntilDateTime":null,"voiceSentence":null,"webHook":null,"_links":{"self":{' \
               '"href":"https:\/\/api-asia-01.twizo.com\/verification\/submit\/asia-01-1.17039.ver5a4f1e3e611be5' \
               '.95998727"}}}'

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), Verification)

    def test_get_WidgetSession(self):
        data = '{"sessionToken":"asia-01_11611310_wid5a558e0a9f4630.57631051143d","applicationTag":"Pthon",' \
               '"bodyTemplate":"Your verification token is %token%","createdDateTime":"2018-01-10T03:52:42+00:00",' \
               '"dcs":null,"language":null,"recipient":"1234000000","sender":"Twizo","senderNpi":null,' \
               '"senderTon":null,"tag":null,"tokenLength":6,"tokenType":"numeric","requestedTypes":["backupcode",' \
               '"sms","call","biovoice"],"allowedTypes":["sms","call"],"validity":null,"status":"no status",' \
               '"statusCode":0,"backupCodeIdentifier":"5a13d5a5f0163","totpIdentifier":null,"verificationIds":[],' \
               '"verification":null,"issuer":"","_links":{"self":{' \
               '"href":"https:\/\/api-asia-01.twizo.com\/v1\/widget\/session\/asia-01_11611310_wid5a558e0a9f4630' \
               '.57631051143d"}}} '

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), WidgetSession)

    def test_get_BackupCode(self):
        data = '{"identifier":"1112356","amountOfCodesLeft":10,"codes":["00000000","11111111","22222222","33333333",' \
               '"44444444","55555555","66666666","77777777","88888888","99999999"],' \
               '"createdDateTime":"2018-01-10T04:05:31+00:00","verification":null,"_links":{"self":{' \
               '"href":"https:\/\/api-asia-01.twizo.com\/v1\/backupcode\/1112356"}}} '

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), BackupCode)

    def test_get_Totp(self):
        data = '{"identifier":"1112356","issuer":"(Twizo Test) Twizo",' \
               '"uri":"otpauth:\/\/totp\/%28Twizo%20Test%29%20Twizo:1112356?secret' \
               '=TESTKEYTESTKEYTESTKEYTESTKEYTESTKEYTESTKEYTESTKEYTES\u0026issuer=%28Twizo%20Test%29%20Twizo",' \
               '"verification":null,"_links":{"self":{"href":"https:\/\/api-asia-01.twizo.com\/totp\/1112356"}}} '

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), Totp)

    def test_get_Totp_response(self):
        data = '{"identifier":"1234","issuer":"(Twizo Test) Twizo","uri":null,"_embedded":{"verification":{' \
               '"applicationTag":"Joomla","bodyTemplate":null,"createdDateTime":"2018-01-10T05:53:06+00:00",' \
               '"dcs":null,"issuer":"","language":null,"messageId":"asia-01-2.16502.ver5a55aa4238a9b9.64195439",' \
               '"reasonCode":null,"recipient":"","salesPrice":null,"salesPriceCurrencyCode":null,"sender":null,' \
               '"senderNpi":null,"senderTon":null,"sessionId":"","status":"success","statusCode":1,"tag":null,' \
               '"tokenLength":null,"tokenType":null,"type":"totp","validity":null,"validUntilDateTime":null,' \
               '"voiceSentence":null,"webHook":null,"_links":{"self":{' \
               '"href":"https:\/\/api-asia-01.twizo.com\/verification\/submit\/asia-01-2.16502.ver5a55aa4238a9b9' \
               '.64195439"}}}},"_links":{"self":{"href":"https:\/\/api-asia-01.twizo.com\/totp\/1234"}}} '

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), TotpResponseSuccess)

    def test_get_BioVoice(self):
        data = '{"createdDateTime":"2018-01-10T08:35:43+00:00","language":null,"reasonCode":null,' \
               '"recipient":"123456789","registrationId":"16502.B015a55d05faef5d5.77600357","salesPrice":null,' \
               '"salesPriceCurrencyCode":null,"status":"no status","statusCode":0,"voiceSentence":"Verify me with my ' \
               'voicepin","webHook":null,"_links":{"self":{' \
               '"href":"https:\/\/api-asia-01.twizo.com\/biovoice\/registration\/16502.B015a55d05faef5d5.77600357"}}} '

        result = self.sut.parse(data)

        # Check if item in items list is parsed to Sms
        self.assertEqual(type(result), BioVoice)


if __name__ == '__main__':
    unittest.main()
