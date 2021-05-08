from resources.concrete.metrics.options import MetricsPossibilities
from resources.context.metrics import Metrics


class MetricCreator:
    @staticmethod
    def create_metric(metric_case: str) -> Metrics:
        metric = MetricsPossibilities.case(metric_case)
        return metric
