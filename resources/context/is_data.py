from abc import ABC, abstractmethod
from typing import Any


class IsData(ABC):
    @abstractmethod
    def is_data(self, data: Any) -> bool:
        pass
