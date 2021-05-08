from resources.context.is_data import IsData
from typing import Any


class IsString(IsData):
    def is_data(self, data: Any) -> bool:
        try:
            str(data)
            return True
        except ValueError:
            return False
