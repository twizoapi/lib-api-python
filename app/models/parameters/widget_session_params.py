class WidgetSessionParams:
    def __init__(self, allowed_types=None, recipient=None):
        self.allowedTypes = allowed_types
        self.recipient = recipient
        self.backupCodeIdentifier = None
        self.tokenLength = None
        self.tokenType = None
        self.tag = None
        self.bodyTemplate = None
        self.sender = None
        self.senderTon = None
        self.senderNpi = None
        self.dcs = None
