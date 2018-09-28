from models import TwizoModel


class Balance(TwizoModel):
    def __init__(self):
        self.credit = 0
        self.currencyCode = ""
        self.freeVerifications = 0
        self.wallet = ""
