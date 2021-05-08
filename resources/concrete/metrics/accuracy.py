from resources.context.metrics import Metrics


class Accuracy(Metrics):
    def __init__(self, metric_value: float) -> None:
        super().__init__(metric_value)
        self.name: str = "accuracy"
        self.min: int = 0
        self.max: int = 1
        self.is_bigger_better: bool = True

    def is_is_range(self) -> bool:
        return self.min <= self.metric_value <= self.max

    def __repr__(self):
        first_part: str = f"\nMetric {self.name} goes from  {self.min} to {self.max}."
        second_part: str = f"\nA bigger valuer is better: {self.is_bigger_better}."
        third_part: str = f"\n{self.name}: {self.metric_value} means {self.metric_value * 100} % score."
        representation: str = first_part + second_part + third_part
        return representation
