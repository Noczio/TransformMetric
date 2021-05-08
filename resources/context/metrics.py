from abc import ABC, abstractmethod

from resources.context.min_max import Limits
from resources.other.load import load_json_file
from resources.other.path import normal_path, debug_path


class Metrics(ABC, Limits):
    is_bigger_better: bool
    name: str

    def __init__(self, metric_value: float):
        self.metric_value = metric_value

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def is_is_range(self) -> bool:
        pass
