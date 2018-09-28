from models import TwizoModel


class BioVoice(TwizoModel):
    def __init__(self):
        self.createdDateTime = None
        self.language = None
        self.reasonCode = None
        self.recipient = None
        self.registrationId = None
        self.salesPrice = None
        self.salesPriceCurrencyCode = None
        self.status = None
        self.statusCode = None
        self.voiceSentence = None
        self.webHook = None
        self._links = None
