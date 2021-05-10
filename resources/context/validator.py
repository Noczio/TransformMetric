from abc import ABC, abstractmethod


class ArgumentValidator(ABC):
    @abstractmethod
    def validate_arguments(self, **kwargs) -> None:
        pass
