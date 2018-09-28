from typing import List


class SmsParams:
    def __init__(self, recipients: List, body: str, sender: str):
        self.recipients = recipients
        self.body = body
        self.sender = sender
        self.senderNpi = None
        self.senderTon = None
        self.pid = None
        self.scheduledDelivery = None
        self.tag = None
        self.validity = None
        self.resultType = None
        self.callbackUrl = None
