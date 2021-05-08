from resources.context.metrics import Metrics


class R2(Metrics):
    def __init__(self) -> None:
        super().__init__()
        self.name: str = "r2"
        self.min: str = "- Infinity"
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        self.metric_value = value
        return True

    def __repr__(self) -> str:
        first_part: str = f"\n{self.name}: {self.metric_value}."
        additional: str = f"Because it is a negative number, it should get fixed to 0." if self.metric_value < 0 \
            else "No Transformation available."
        representation: str = first_part + " " + additional
        return representation
