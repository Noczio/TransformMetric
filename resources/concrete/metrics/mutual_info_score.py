from resources.context.metrics import Metrics


class MutualInfoScore(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "mutual info score"
        self.min: int = 0
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = False

    def is_is_range(self, value: float) -> bool:
        return value >= self.min