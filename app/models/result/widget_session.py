from models import TwizoModel


class WidgetSession(TwizoModel):
    def __init__(self):
        self.sessionToken = None
        self.applicationTag = None
        self.bodyTemplate = None
        self.createdDateTime = None
        self.dcs = None
        self.language = None
        self.recipient = None
        self.sender = None
        self.senderNpi = None
        self.senderTon = None
        self.tag = None
        self.tokenLength = None
        self.tokenType = None
        self.requestedTypes = None
        self.allowedTypes = None
        self.validity = None
        self.status = None
        self.statusCode = None
        self.totpIdentifier = None
        self.backupCodeIdentifier = None
        self.verificationIds = None
        self.verification = None
        self.issuer = None
        self._links = None
