from resources.context.metrics import Metrics


class ExplainedVariance(Metrics):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "explained variance"
        self.min: str = "- Infinity"
        self.max: int = 1
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return self.metric_value <= self.max

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.metric_value}. No transformation available."
        return representation
