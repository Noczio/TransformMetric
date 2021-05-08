from resources.context.metrics import Metrics


class RocAuc(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "roc auc"
        self.min: int = 0
        self.max: int = 1
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        return self.min <= value <= self.max
