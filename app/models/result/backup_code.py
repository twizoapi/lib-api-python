from models import TwizoModel


class BackupCode(TwizoModel):
    def __init__(self):
        self.identifier = None
        self.amountOfCodesLeft = None
        self.codes = None
        self.createdDateTime = None
        self.verification = None
        self._links = None
