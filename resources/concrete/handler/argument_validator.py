from resources.other.load import load_json_file
from resources.other.metric_valid import is_metric_name_valid
from resources.other.path import execution_metric_options
from resources.context.handler import ArgumentHandler
from resources.concrete.is_data.caller import IsDataValid


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
            print(f"Input: {metric_name} is not a ml metric or it is not implemented. Use one of the following metrics:"
                  f" {self._valid_metrics}")


def print_metric(metric_name: str, metric_values: tuple) -> None:
    for value in metric_values:
        if IsDataValid.is_data("number", value):
            metric = MetricCreator.create_metric(metric_name, float(value))
            if metric.is_is_range():
                print(metric)
            else:
                print(f"{metric_name} does not allow input {value}")
