from abc import ABC, abstractmethod
from resources.other.load import load_json_file
from resources.other.path import normal_path, debug_path


class SysData(ABC):
    @abstractmethod
    def parameters_are_valid(self, *args) -> bool:
        pass
