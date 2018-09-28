from models import TwizoModel


class Totp(TwizoModel):
    def __init__(self):
        self.identifier = None
        self.issuer = None
        self.uri = None
        self.verification = None
        self._links = None


class TotpResponseSuccess(TwizoModel):
    def __init__(self):
        self.identifier = None
        self.issuer = None
        self.uri = None
        self._embedded = None
        self._links = None
