from typing import Any

from resources.context.is_data import IsData


class IsNumeric(IsData):
    def is_data_valid(self, data: Any) -> bool:
        try:
            float(data)
            return True
        except ValueError:
            return False
