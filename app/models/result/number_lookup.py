from models import TwizoModel


class NumberLookup(TwizoModel):
    def __init__(self):
        self.applicationTag = None
        self.callbackUrl = None
        self.countryCode = None
        self.createdDateTime = None
        self.imsi = None
        self.isPorted = None
        self.isRoaming = None
        self.messageId = None
        self.msc = None
        self.networkCode = None
        self.number = None
        self.operator = None
        self.reasonCode = None
        self.resultTimestamp = None
        self.resultType = None
        self.salesPrice = None
        self.salesPriceCurrencyCode = None
        self.status = None
        self.statusCode = None
        self.tag = None
        self.validity = None
        self.validUntilDateTime = None
        self._links = None
