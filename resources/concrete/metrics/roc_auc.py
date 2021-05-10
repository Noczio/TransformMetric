from resources.context.metrics import Metrics


class RocAuc(Metrics):
    def __init__(self) -> None:
        super().__init__("classification", "roc_auc")

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.min <= self.score <= self.max

    def __enter__(self) -> "Metrics":
        first_part: str = f"\nMetric {self.name} goes from {self.min} to {self.max}."
        adaptive_text = "bigger" if self.bigger_is_better else "smaller"
        second_part: str = f"A {adaptive_text} value is better. This metric shows the trade-off between sensitivity " \
                           f"(TPR) and specificity (1 – FPR)."
        output = first_part + " " + second_part + "\n"
        print(output)
        return self

    def __repr__(self) -> str:
        representation: str = f"{self.score} means {self.score * 100} % score under the roc curve."
        return representation
