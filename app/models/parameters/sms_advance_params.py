from typing import List

from models.parameters import SmsParams


class SmsAdvanceParams(SmsParams):
    def __init__(self, recipients: List or str, body: str, sender: str):
        super().__init__(recipients, body, sender)
        self.udh = None
        self.dcs = None
