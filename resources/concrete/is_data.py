from resources.context.is_data import IsData
from typing import Any


class IsString(IsData):
    def is_data(self, data: Any) -> bool:
        try:
            str(data)
            return True
        except ValueError:
            return False


class IsNumeric(IsData):
    def is_data(self, data: Any) -> bool:
        try:
            float(data)
            return True
        except ValueError:
            return False


class IsDataValid:
    @staticmethod
    def is_data(data_validator: IsData, data: Any) -> bool:
        return data_validator.is_data(data)
