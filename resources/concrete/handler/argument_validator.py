from resources.concrete.metrics.options import MetricsPossibilities
from resources.context.handler import ArgumentHandler
from resources.other.show import show_metrics
from resources.other.valid import is_metric_name_valid


class SysValidator(ArgumentHandler):
    def __init__(self) -> None:
        self._valid_metrics = MetricsPossibilities.available_cases()

    def handle_arguments(self, metric_name: str, metric_values: tuple) -> None:
        if is_metric_name_valid(metric_name, self._valid_metrics):
            show_metrics(metric_name, metric_values)
        else:
            print(f"\nInput \"{metric_name}\" is not a ML metric or it is not implemented yet. Use one of the "
                  f"following metrics:\n{self._valid_metrics}")
