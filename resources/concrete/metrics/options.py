from resources.context.metrics import Metrics
from resources.context.switch import Switch
from resources.concrete.metrics.roc_auc import RocAuc
from resources.concrete.metrics.accuracy import Accuracy
from resources.concrete.metrics.r2_score import R2
from resources.concrete.metrics.mean_squared_error import MeanSquaredError
from resources.concrete.metrics.neg_mean_squared_error import NegMeanSquaredError
from resources.concrete.metrics.explained_variance import ExplainedVariance
from resources.concrete.metrics.mutual_info_score import MutualInfoScore
from resources.concrete.metrics.completeness_score import CompletenessScore


class MetricsPossibilities(Switch):

    @staticmethod
    def roc_auc(debug: bool = False) -> Metrics:
        return RocAuc(debug)

    @staticmethod
    def accuracy(debug: bool = False) -> Metrics:
        return Accuracy(debug)

    @staticmethod
    def r2(debug: bool = False) -> Metrics:
        return R2(debug)

    @staticmethod
    def mean_squared_error(debug: bool = False) -> Metrics:
        return MeanSquaredError(debug)

    @staticmethod
    def neg_mean_squared_error(debug: bool = False) -> Metrics:
        return NegMeanSquaredError(debug)

    @staticmethod
    def explained_variance(debug: bool = False) -> Metrics:
        return ExplainedVariance(debug)

    @staticmethod
    def mutual_info_score(debug: bool = False) -> Metrics:
        return MutualInfoScore(debug)

    @staticmethod
    def completeness_score(debug: bool = False) -> Metrics:
        return CompletenessScore(debug)
