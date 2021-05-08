from resources.context.metrics import Metrics
from resources.context.switch import Switch
from resources.concrete.metrics.roc_auc import RocAuc
from resources.concrete.metrics.accuracy import Accuracy
from resources.concrete.metrics.r2_score import R2
from resources.concrete.metrics.mean_squared_error import MeanSquaredError
from resources.concrete.metrics.neg_mean_squared_error import NegMeanSquaredError
from resources.concrete.metrics.explained_variance import ExplainedVariance
from resources.concrete.metrics.completeness_score import CompletenessScore


class MetricsPossibilities(Switch):

    @staticmethod
    def roc_auc(metric_value: float) -> Metrics:
        return RocAuc(metric_value)

    @staticmethod
    def accuracy(metric_value: float) -> Metrics:
        return Accuracy(metric_value)

    @staticmethod
    def r2(metric_value: float) -> Metrics:
        return R2(metric_value)

    @staticmethod
    def mean_squared_error(metric_value: float) -> Metrics:
        return MeanSquaredError(metric_value)

    @staticmethod
    def neg_mean_squared_error(metric_value: float) -> Metrics:
        return NegMeanSquaredError(metric_value)

    @staticmethod
    def explained_variance(metric_value: float) -> Metrics:
        return ExplainedVariance(metric_value)

    @staticmethod
    def completeness_score(metric_value: float) -> Metrics:
        return CompletenessScore(metric_value)
