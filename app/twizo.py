from controllers import *
from service import TwizoService
from worker import HttpClient


class Twizo:
    def __init__(self, api_key, api_host):
        worker = HttpClient(api_key, api_host)
        twizo_service = TwizoService()

        self.widget_register_session_controller = WidgetRegisterSessionController(worker, twizo_service)
        self.widget_session_controller = WidgetSessionController(worker, twizo_service)
        self.number_lookup_controller = NumberLookupController(worker, twizo_service)
        self.verification_controller = VerificationController(worker, twizo_service)
        self.application_controller = ApplicationController(worker, twizo_service)
        self.backup_code_controller = BackupCodeController(worker, twizo_service)
        self.bio_voice_controller = BioVoiceController(worker, twizo_service)
        self.balance_controller = BalanceController(worker, twizo_service)
        self.totp_controller = TotpController(worker, twizo_service)
        self.sms_controller = SmsController(worker, twizo_service)
