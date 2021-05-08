from resources.context.metrics import Metrics


class Accuracy(Metrics):
    def __init__(self) -> None:
        super().__init__("classification", "accuracy")

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.min <= self.score <= self.max

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.score} means {self.score * 100} % score."
        return representation
