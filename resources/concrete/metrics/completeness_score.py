from resources.context.metrics import Metrics


class CompletenessScore(Metrics):
    def __init__(self, debug: bool = False) -> None:
        super().__init__("clustering", "completeness_score", debug)

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.min <= self.score <= self.max

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.score} means {self.score * 100} % score."
        return representation
