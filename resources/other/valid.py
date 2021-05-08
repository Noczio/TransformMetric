from resources.concrete.is_data.caller import IsDataValid


def is_metric_name_valid(metric_name: str, valid_metrics: tuple) -> bool:
    is_string: bool = IsDataValid.is_data("string", metric_name)
    is_valid_metric: bool = True if is_string and metric_name in valid_metrics else False
    return is_valid_metric
