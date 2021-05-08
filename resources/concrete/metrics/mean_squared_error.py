from resources.context.metrics import Metrics


class MeanSquaredError(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "mean squared error"
        self.min: int = 0
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = False

    def is_is_range(self, value: float) -> bool:
        return value >= self.min
