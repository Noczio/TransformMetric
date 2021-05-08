from resources.context.metrics import Metrics


class R2(Metrics):
    def __init__(self, metric_value: float):
        super().__init__(metric_value)
        self.name: str = "r2"
        self.min: str = "- Infinity"
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = True

    def is_is_range(self) -> bool:
        return True

    def __repr__(self):
        first_part: str = f"\nMetric {self.name} goes from  {self.min} to {self.max}."
        second_part: str = f"\nA bigger valuer is better: {self.is_bigger_better}."
        third_part: str = f"\n{self.name}: {self.metric_value}."
        additional: str = f"Because it is a negative number, it gets fixed to 0." if self.metric_value < 0 \
            else "No Transformation available"
        representation: str = first_part + second_part + third_part + additional
        return representation
