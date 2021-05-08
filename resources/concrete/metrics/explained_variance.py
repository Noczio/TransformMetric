from resources.context.metrics import Metrics


class ExplainedVariance(Metrics):
    def __init__(self) -> None:
        super().__init__(metric_value)
        self.name: str = "explained variance"
        self.min: str = "- Infinity"
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return True

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.metric_value}. No transformation available."
        return representation
