from abc import ABC, abstractmethod


class ArgumentHandler(ABC):
    def __init__(self, debug: bool = False) -> None:
        self._debug = debug

    @abstractmethod
    def handle_arguments(self, *args) -> None:
        pass
