from typing import Any

from resources.concrete.is_data.options import IsDataPossibilities


class IsDataValid:
    @staticmethod
    def is_data(validation_case: str, data: Any) -> bool:
        validator: IsData = IsDataPossibilities.case(validation_case)
        return validator.is_data(data)
