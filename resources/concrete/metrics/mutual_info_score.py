from resources.context.metrics import Metrics


class MutualInfoScore(Metrics):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "mutual info score"
        self.min: int = 0
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = False

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return self.metric_value >= self.min

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.metric_value}. No transformation available."
        return representation
