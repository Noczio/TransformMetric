from resources.concrete.metrics.caller import MetricCreator
from resources.other.is_valid import is_metric_name_valid, is_metric_values_valid
from resources.other.load import load_json_file
from resources.other.path import execution_metric_options


class SysValidator:

    def __init__(self, debug: bool = False) -> None:
        metrics_path: str = execution_metric_options[debug]
        data: dict = load_json_file(metrics_path)
        self.valid_metrics = tuple([metric for all_values in data.values() for metric in all_values.keys()])

    def is_valid(self, metric_name: str, metric_values: tuple) -> bool:
        if is_metric_name_valid(metric_name, self.valid_metrics):
            return is_metric_values_valid(metric_values, MetricCreator.create_metric(metric_name))
        return False
