from abc import ABC, abstractmethod
from typing import Any


class IsData(ABC):
    @abstractmethod
    def is_data_valid(self, data: Any) -> bool:
        pass
