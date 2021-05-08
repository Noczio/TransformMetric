from resources.concrete.is_data.options import IsDataPossibilities
from typing import Any


class IsDataValid:
    @staticmethod
    def is_data(data_validator: str, data: Any) -> bool:
        validator: IsData = IsDataPossibilities.case(data_validator)
        return validator.is_data(data)
