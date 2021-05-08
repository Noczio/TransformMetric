from resources.concrete.is_data.caller import IsDataValid
from resources.context.metrics import Metrics


def is_metric_name_valid(metric_name: str, valid_metrics: tuple) -> bool:
    is_string: bool = IsDataValid.is_data("string", metric_name)
    is_valid_metric: bool = True if is_string and metric_name in valid_metrics else False
    return is_valid_metric


def is_metric_values_valid(metric_values: tuple, metric: Metrics) -> bool:
    for value in metric_values:
        is_float: bool = IsDataValid.is_data("number", value)
        is_valid: bool = True if is_float and metric.is_is_range(float(value)) else False
        if not is_valid:
            return False
    return True
