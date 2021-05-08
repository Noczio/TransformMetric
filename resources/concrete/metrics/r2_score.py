from resources.context.metrics import Metrics


class R2(Metrics):
    def __init__(self, debug: bool = False) -> None:
        super().__init__("regression", "r2", debug)

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return True

    def __repr__(self) -> str:
        first_part: str = f"\n{self.name}: {self.score}."
        additional: str = f"Because it is a negative number, it should get fixed to 0." if self.score < 0 \
            else "No Transformation available."
        representation: str = first_part + " " + additional
        return representation
