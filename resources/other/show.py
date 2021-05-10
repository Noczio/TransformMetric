from resources.concrete.is_data.caller import IsDataCreator
from resources.concrete.metrics.caller import MetricCreator
from resources.context.is_data import IsData


def show_metrics(metric_name: str, metric_values: tuple) -> None:
    with MetricCreator.create_metric(metric_name) as metric:
        data_validator: IsData = IsDataCreator.create_data_validator("number")
        for value in metric_values:
            if data_validator.is_data_valid(value) and metric.score_in_range(float(value)):
                print(metric)
            else:
                print(f"metric does not allow input \"{value}\"")
