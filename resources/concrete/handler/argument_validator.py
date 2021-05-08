from resources.concrete.is_data.caller import IsDataValid
from resources.concrete.metrics.caller import MetricCreator
from resources.context.handler import ArgumentHandler
from resources.other.load import load_json_file
from resources.other.metric_valid import is_metric_name_valid
from resources.other.path import execution_metric_options


class SysValidator(ArgumentHandler):
    def __init__(self, debug: bool = False) -> None:
        super().__init__(debug)
        metrics_path: str = execution_metric_options[self._debug]
        data: dict = load_json_file(metrics_path)
        self._valid_metrics = tuple([metric for all_values in data.values() for metric in all_values.keys()])

    def handle_arguments(self, metric_name: str, metric_values: tuple) -> None:
        if is_metric_name_valid(metric_name, self._valid_metrics):
            print_metric(metric_name, metric_values)
        else:
            print(f"\nInput: {metric_name} is not a ML metric or it is not implemented yet. Use one of the following"
                  f" metrics:\n{self._valid_metrics}")


def print_metric(metric_name: str, metric_values: tuple) -> None:
    metric = MetricCreator.create_metric(metric_name)
    metric.header_info()
    for value in metric_values:
        if IsDataValid.is_data("number", value) and metric.is_is_range(float(value)):
            print(metric)
        else:
            print(f"\n{metric.name} does not allow input: {value}")
