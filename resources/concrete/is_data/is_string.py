from typing import Any

from resources.context.is_data import IsData


class IsString(IsData):
    def is_data_valid(self, data: Any) -> bool:
        try:
            str(data)
            return True
        except ValueError:
            return False
