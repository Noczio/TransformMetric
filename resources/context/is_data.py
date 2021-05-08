from abc import ABC, abstractmethod


class IsData(ABC):
    @abstractmethod
    def is_data(self, *args, **kwargs) -> bool:
        pass
