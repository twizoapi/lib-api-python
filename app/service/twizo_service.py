import json
from abc import ABCMeta
from json import JSONDecodeError
from typing import List

from exceptions import TwizoDataException, TwizoJsonException
from models import TwizoModel


class TwizoService(metaclass=ABCMeta):
    def __init__(self):
        self.object_type = TwizoModel

    def _parse_json(self, data: dict) -> object:
        """
            Convert input dict to TwizoModel if structure is recognised and exists. Else returns a global TwizoModel.
        Args:
            data: Dict to be converted

        Returns:
            Object
        """
        if self.object_type == list:
            return list(data.values())

        # Check if the structure of the data is equal to an existing TwizoModel subclass
        # If it is equal -> set the result to this type.
        models = [cls() for cls in TwizoModel.__subclasses__()]
        for model in models:
            if data.keys() == model.__dict__.keys():
                model.__dict__.update(data)
                return model

        # Set result to default on given type.
        result = self.object_type()
        if isinstance(result, TwizoModel):
            result.__dict__.update(data)

        return result

    def parse(self, data: str, object_type: object = None) -> TwizoModel or List:
        """
        Parse the json data to a TwizoModel

        Args:
            data: JSON data to be parsed
            object_type: ObjectType which need to be parsed.

        Raises:
            TwizoDataException
            TwizoJsonException

        Returns:
            TwizoModel
        """
        if object_type is not None:
            self.object_type = object_type

        if "" == data or data is None:
            raise TwizoDataException("Twizo didn't collect any data. Unexpected please try again.")

        try:
            return json.loads(data, object_hook=self._parse_json)
        except JSONDecodeError as exception:
            raise TwizoJsonException(exception.msg)
