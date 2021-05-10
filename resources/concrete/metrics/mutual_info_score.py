from resources.context.metrics import Metrics


class MutualInfoScore(Metrics):
    def __init__(self) -> None:
        super().__init__("clustering", "mutual_info_score")

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.score >= self.min

    def __repr__(self) -> str:
        representation: str = f"{self.score}. No transformation available."
        return representation
