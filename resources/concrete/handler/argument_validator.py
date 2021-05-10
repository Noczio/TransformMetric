from resources.concrete.metrics.options import MetricsPossibilities
from resources.context.validator import ArgumentValidator
from resources.other.show import show_metrics
from resources.other.valid import is_metric_name_valid


class SysArgumentValidator(ArgumentValidator):
    def __init__(self) -> None:
        self._valid_metrics = MetricsPossibilities.available_cases()
        self._valid_kwargs = ("metric_name",  "metric_values")

    def validate_arguments(self, **kwargs) -> None:
        metric_name: str = kwargs["metric_name"]
        metric_value: tuple = kwargs["metric_value"]
        valid_metric: tuple = self._valid_metrics
        if is_metric_name_valid(metric_name, valid_metric):
            show_metrics(metric_name, metric_value)
        else:
            print(f"\nInput \"{metric_name}\" is not a ML metric or it is not implemented yet. Use one of the "
                  f"following metrics:\n\n{valid_metric}")
