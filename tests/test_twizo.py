import unittest

from controllers import *
from twizo import Twizo


class TwizoTest(unittest.TestCase):
    def test_init(self):
        sut = Twizo("apikey", "apiHost")
        self.assertEqual(type(sut.widget_session_controller), WidgetSessionController)
        self.assertEqual(type(sut.number_lookup_controller), NumberLookupController)
        self.assertEqual(type(sut.verification_controller), VerificationController)
        self.assertEqual(type(sut.application_controller), ApplicationController)
        self.assertEqual(type(sut.backup_code_controller), BackupCodeController)
        self.assertEqual(type(sut.bio_voice_controller), BioVoiceController)
        self.assertEqual(type(sut.balance_controller), BalanceController)
        self.assertEqual(type(sut.totp_controller), TotpController)
        self.assertEqual(type(sut.sms_controller), SmsController)


if __name__ == '__main__':
    unittest.main()
