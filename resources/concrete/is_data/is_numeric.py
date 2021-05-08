from resources.context.is_data import IsData
from typing import Any


class IsNumeric(IsData):
    def is_data(self, data: Any) -> bool:
        try:
            float(data)
            return True
        except ValueError:
            return False