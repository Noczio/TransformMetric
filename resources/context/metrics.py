from abc import ABC, abstractmethod

from resources.context.min_max import Limits
from resources.other.load import load_json_file
from resources.other.path import normal_path, debug_path


class Metrics(ABC, Limits):
    is_bigger_better: bool
    metric_value: float
    name: str

    def header_info(self) -> None:
        first_part: str = f"\nMetric {self.name} goes from {self.min} to {self.max}."
        adaptive_text = "bigger" if self.is_bigger_better else "smaller"
        second_part: str = " " + f"A {adaptive_text} value is better."
        output = first_part + second_part
        print(output)

    @abstractmethod
    def is_is_range(self, value: float) -> bool:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
