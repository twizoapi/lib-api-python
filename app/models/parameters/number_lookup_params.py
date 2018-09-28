from typing import List


class NumberLookupParams:
    def __init__(self, numbers: List):
        self.numbers = numbers
        self.tag = None
        self.validity = None
        self.resultType = None
        self.callbackUrl = None
