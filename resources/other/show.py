from resources.concrete.is_data.caller import IsDataValid
from resources.concrete.metrics.caller import MetricCreator


def show_metrics(metric_name: str, metric_values: tuple) -> None:
    with MetricCreator.create_metric(metric_name) as metric:
        for value in metric_values:
            if IsDataValid.is_data("number", value) and metric.score_in_range(float(value)):
                print(metric)
            else:
                print(f"\n{metric.name} does not allow input: {value}")
