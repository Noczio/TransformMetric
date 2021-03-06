from resources.concrete.metrics.accuracy import Accuracy
from resources.concrete.metrics.completeness_score import CompletenessScore
from resources.concrete.metrics.explained_variance import ExplainedVariance
from resources.concrete.metrics.mean_squared_error import MeanSquaredError
from resources.concrete.metrics.mutual_info_score import MutualInfoScore
from resources.concrete.metrics.neg_mean_squared_error import NegMeanSquaredError
from resources.concrete.metrics.r2_score import R2
from resources.concrete.metrics.roc_auc import RocAuc
from resources.context.metrics import Metrics
from resources.context.switch import Switch


class MetricsPossibilities(Switch):

    @staticmethod
    def roc_auc() -> Metrics:
        return RocAuc()

    @staticmethod
    def accuracy() -> Metrics:
        return Accuracy()

    @staticmethod
    def r2() -> Metrics:
        return R2()

    @staticmethod
    def mean_squared_error() -> Metrics:
        return MeanSquaredError()

    @staticmethod
    def neg_mean_squared_error() -> Metrics:
        return NegMeanSquaredError()

    @staticmethod
    def explained_variance() -> Metrics:
        return ExplainedVariance()

    @staticmethod
    def mutual_info_score() -> Metrics:
        return MutualInfoScore()

    @staticmethod
    def completeness_score() -> Metrics:
        return CompletenessScore()
