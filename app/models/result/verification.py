from models import TwizoModel


class Verification(TwizoModel):
    def __init__(self):
        self.applicationTag = None
        self.bodyTemplate = None
        self.createdDateTime = None
        self.dcs = None
        self.issuer = None
        self.language = None
        self.messageId = None
        self.reasonCode = None
        self.recipient = None
        self.salesPrice = None
        self.salesPriceCurrencyCode = None
        self.sender = None
        self.senderNpi = None
        self.senderTon = None
        self.sessionId = None
        self.status = None
        self.statusCode = None
        self.tag = None
        self.tokenLength = None
        self.tokenType = None
        self.type = None
        self.validity = None
        self.validUntilDateTime = None
        self.voiceSentence = None
        self.webHook = None
        self._links = None
