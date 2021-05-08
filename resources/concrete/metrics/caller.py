from resources.concrete.metrics.options import MetricsPossibilities
from resources.context.metrics import Metrics


class MetricCreator:
    @staticmethod
    def create_metric(metric_case: str, metric_value: float) -> Metrics:
        metric = MetricsPossibilities.case(metric_case, metric_value)
        return metric
