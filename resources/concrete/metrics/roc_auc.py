from resources.context.metrics import Metrics


class RocAuc(Metrics):
    def __init__(self, debug: bool = False) -> None:
        super().__init__("classification", "roc_auc", debug)

    def score_in_range(self, score: float) -> bool:
        self.score = score
        return self.min <= self.score <= self.max

    def header_info(self) -> None:
        first_part: str = f"\nMetric {self.name} goes from {self.min} to {self.max}."
        adaptive_text = "bigger" if self.is_bigger_better else "smaller"
        second_part: str = f"A {adaptive_text} value is better. This metric shows the trade-off between sensitivity " \
                           f"(TPR) and specificity (1 – FPR)."
        output = first_part + " " + second_part
        print(output)

    def __repr__(self) -> str:
        representation: str = f"\n{self.name}: {self.score} means {self.score * 100} % score under the roc curve."
        return representation
