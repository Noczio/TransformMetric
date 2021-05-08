from abc import ABC, abstractmethod
from resources.other.load import load_json_file
from resources.other.path import normal_path, debug_path


class ArgumentHandler(ABC):

    def __init__(self, debug: bool = False) -> None:
        self._debug = debug

    @abstractmethod
    def handle_arguments(self, *args) -> None:
        pass
