from resources.context.metrics import Metrics


class MutualInfoScore(Metrics):
    def __init__(self, metric_value: float):
        super().__init__(metric_value)
        self.name: str = "mutual info score"
        self.min: int = 0
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = False

    def is_is_range(self) -> bool:
        return self.metric_value >= self.min

    def __repr__(self):
        first_part: str = f"\nMetric {self.name} goes from  {self.min} to {self.max}."
        second_part: str = f"\nA bigger valuer is better: {self.is_bigger_better}."
        third_part: str = f"\n{self.name}: {self.metric_value}. No transformation available."
        representation: str = first_part + second_part + third_part
        return representation
