from resources.concrete.metrics.options import MetricsPossibilities
from resources.context.metrics import Metrics


class MetricCreator:
    @staticmethod
    def create_metric(metric_case: str, debug: bool = False) -> Metrics:
        metric = MetricsPossibilities.case(metric_case, debug)
        return metric
