from resources.context.metrics import Metrics


class R2(Metrics):
    def __init__(self):
        super().__init__()
        self.name: str = "r2"
        self.min: str = "- Infinity"
        self.max: str = "+ Infinity"
        self.is_bigger_better: bool = True

    def is_is_range(self, value: float) -> bool:
        return True
