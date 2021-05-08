from abc import ABC, abstractmethod

from resources.context.min_max import Limits
from resources.other.load import load_json_file
from resources.other.path import normal_path, debug_path


class Metrics(ABC, Limits):
    _changing_text: dict = {True: "A bigger valuer is better.", False: "A smaller value is better."}
    is_bigger_better: bool
    name: str

    def __repr__(self) -> str:
        first_part: str = f"Metric {self.name} goes from  {self.min} to {self.max}."
        representation: str = first_part + " " + self._changing_text[self.is_bigger_better]
        return representation

    @abstractmethod
    def is_is_range(self, value: float) -> bool:
        pass
