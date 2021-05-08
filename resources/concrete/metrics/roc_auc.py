from resources.context.metrics import Metrics


class RocAuc(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "roc auc"
        self.min: int = 0
        self.max: int = 1
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return self.min <= self.metric_value <= self.max

    def header_info(self) -> None:
        first_part: str = f"\nMetric {self.name} goes from {self.min} to {self.max}."
        adaptive_text = "bigger" if self.is_bigger_better else "smaller"
        second_part: str = f"A {adaptive_text} value is better. This metric shows the trade-off between sensitivity " \
                           f"(TPR) and specificity (1 – FPR)."
        output = first_part + " " + second_part
        print(output)

    def __repr__(self):
        representation: str = f"\n{self.name}: {self.metric_value} means {self.metric_value * 100} % score."
        return representation
