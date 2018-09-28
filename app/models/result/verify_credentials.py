from models import TwizoModel


class VerifyCredentials(TwizoModel):
    def __init__(self):
        self.applicationTag = ""
        self.isTestKey = False
