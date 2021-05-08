from resources.context.metrics import Metrics


class MeanSquaredError(Metrics):
    def __init__(self, debug: bool = False) -> None:
        super().__init__("regression", "mean_squared_error", debug)

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.score >= self.min

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.score} is the same as mean absolute error " \
                              f"{self.score ** 2}."
        return representation
