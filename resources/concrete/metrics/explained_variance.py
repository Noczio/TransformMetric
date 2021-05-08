from resources.context.metrics import Metrics


class ExplainedVariance(Metrics):
    def __init__(self, debug: bool = False) -> None:
        super().__init__("regression", "explained_variance", debug)

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.score <= self.max

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.score}. No transformation available."
        return representation
