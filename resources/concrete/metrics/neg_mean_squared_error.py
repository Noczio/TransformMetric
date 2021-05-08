from resources.context.metrics import Metrics


class NegMeanSquaredError(Metrics):
    def __init__(self) -> None:
        super().__init__("regression", "neg_mean_squared_error")

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.score <= self.max

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.score} is the same as mean squared error, but negated."
        return representation
