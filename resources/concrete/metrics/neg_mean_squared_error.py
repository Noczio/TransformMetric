from resources.context.metrics import Metrics


class NegMeanSquaredError(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "neg mean squared error (NMSE)"
        self.min: str = "- Infinity"
        self.max: int = 0
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return self.metric_value <= self.max

    def __repr__(self):
        representation: str = f"\n{self.name}: {self.metric_value} is the same mean squared error " \
                              f"(MSE), but negated."
        return representation
