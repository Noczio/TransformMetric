from resources.context.metrics import Metrics


class NegMeanSquaredError(Metrics):
    def __init__(self, metric_value: float):
        super().__init__(metric_value)
        self.name: str = "neg mean squared error (NMSE)"
        self.min: str = "- Infinity"
        self.max: int = 0
        self.is_bigger_better: bool = True

    def is_is_range(self) -> bool:
        return self.metric_value <= self.max

    def __repr__(self):
        first_part: str = f"\nMetric {self.name} goes from  {self.min} to {self.max}."
        second_part: str = f"\nA bigger valuer is better: {self.is_bigger_better}."
        third_part: str = f"\n{self.name}: {self.metric_value} is the same mean squared error " \
                          f"{self.metric_value*-1} (MSE), but negated."
        representation: str = first_part + second_part + third_part
        return representation

