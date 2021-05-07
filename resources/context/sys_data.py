from abc import ABC, abstractmethod
from resources.concrete.funcs.load import load_json_file
from resources.other.path import application_path, debug_path
import sys


class SysData(ABC):
    def __init__(self, debug: bool = False):
        options: dict = {True: debug_path["Metrics"]["Path"], False: application_path["Metrics"]["Path"]}
        metrics_path: str = options[debug]
        data: dict = load_json_file(metrics_path)
        self.metrics = [metric for all_values in data.values() for metric in all_values.keys()]

    @abstractmethod
    def parameters_are_valid(self, *args) -> bool:
        pass
