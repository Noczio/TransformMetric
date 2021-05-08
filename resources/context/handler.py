from abc import ABC, abstractmethod


class ArgumentHandler(ABC):
    @abstractmethod
    def handle_arguments(self, *args) -> None:
        pass
