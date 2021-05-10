from resources.context.metrics import Metrics


class MeanSquaredError(Metrics):
    def __init__(self) -> None:
        super().__init__("regression", "mean_squared_error")

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.score >= self.min

    def __repr__(self) -> str:
        representation: str = f"{self.score} is the same as mean absolute error {self.score ** 2}."
        return representation
