from typing import Any

from resources.context.is_data import IsData


class IsString(IsData):
    def is_data(self, data: Any) -> bool:
        try:
            str(data)
            return True
        except ValueError:
            return False
