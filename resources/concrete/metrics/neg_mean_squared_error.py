from resources.context.metrics import Metrics


class NegMeanSquaredError(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "neg mean squared error"
        self.min: str = "- Infinity"
        self.max: int = 0
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        return value <= self.max
