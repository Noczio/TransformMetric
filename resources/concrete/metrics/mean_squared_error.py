from resources.context.metrics import Metrics


class MeanSquaredError(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "mean squared error (MSE)"
        self.min: int = 0
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = False

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return self.metric_value >= self.min

    def __repr__(self):
        representation: str = f"\n{self.name}: {self.metric_value} is the same as mean absolute error " \
                              f"{self.metric_value ** 2} (MAE)."
        return representation
