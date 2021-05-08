from resources.concrete.metrics.options import MetricsPossibilities
from resources.context.metrics import Metrics


class MetricCreator:
    @staticmethod
    def create_metric(metric_type: str, debug: bool = False) -> Metrics:
        metric = MetricsPossibilities.case(metric_type, debug)
        return metric
