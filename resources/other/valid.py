from resources.concrete.is_data.caller import IsDataCreator
from resources.context.is_data import IsData


def is_metric_name_valid(metric_name: str, valid_metrics: tuple) -> bool:
    data_validator: IsData = IsDataCreator.create_data_validator("string")
    is_string: bool = True if data_validator.is_data_valid(metric_name) else False
    is_valid_metric: bool = True if is_string and metric_name in valid_metrics else False
    return is_valid_metric
