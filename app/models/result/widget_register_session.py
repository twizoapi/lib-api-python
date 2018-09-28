from models import TwizoModel


class WidgetRegisterSession(TwizoModel):
    def __init__(self):
        self.sessionToken = None
        self.applicationTag = None
        self.requestedTypes = None
        self.registeredTypes = None
        self.allowedTypes = None
        self.recipient = None
        self.totpIdentifier = None
        self.backupCodeIdentifier = None
        self.issuer = None
        self.language = None
        self.status = None
        self.statusCode = None
        self.createdDateTime = None
        self._links = None
