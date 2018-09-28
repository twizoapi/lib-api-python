from models import TwizoModel


class Sms(TwizoModel):
    def __init__(self):
        self.applicationTag = None
        self.body = None
        self.callbackUrl = None
        self.createdDateTime = None
        self.dcs = None
        self.messageId = None
        self.networkCode = None
        self.pid = None
        self.reasonCode = None
        self.recipient = None
        self.resultType = None
        self.salesPrice = None
        self.salesPriceCurrencyCode = None
        self.scheduledDelivery = None
        self.sender = None
        self.senderNpi = None
        self.senderTon = None
        self.status = None
        self.statusCode = None
        self.tag = None
        self.resultTimestamp = None
        self.udh = None
        self.validity = None
        self.validUntilDateTime = None
        self._links = None
