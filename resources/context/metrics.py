from abc import ABC, abstractmethod
from typing import Any

import resources.concrete.status.mode as app_status
from resources.context.min_max import Limits
from resources.other.load import load_json_file
from resources.other.path import execution_metric_options


class Metrics(ABC, Limits):
    def __init__(self, problem_name: str, metric_name: str):
        metric_path: str = execution_metric_options[app_status.debug]
        metric_data: dict = load_json_file(metric_path)
        prediction_data: dict = metric_data[problem_name]

        self.score: float = 0
        self.name: str = metric_name
        self.min: Any = prediction_data[self.name]["min"]
        self.max: Any = prediction_data[self.name]["max"]
        self.bigger_is_better: bool = prediction_data[self.name]["bigger_is_better"]

    def __enter__(self) -> "Metrics":
        first_part: str = f"\nMetric {self.name} goes from {self.min} to {self.max}."
        adaptive_text = "bigger" if self.bigger_is_better else "smaller"
        second_part: str = f"A {adaptive_text} value is better."
        output = first_part + " " + second_part + "\n"  # this last \n is for aesthetic purposes
        print(output)
        return self

    def __exit__(self, *args) -> None:
        pass

    @abstractmethod
    def score_in_range(self, score: float) -> bool:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass
