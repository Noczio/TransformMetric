import unittest
from resources.concrete.metrics.options import MetricsPossibilities


class MyTestCase(unittest.TestCase):
    def test_something(self):
        expected = ('accuracy', 'completeness_score', 'explained_variance', 'mean_squared_error', 'mutual_info_score',
                    'neg_mean_squared_error', 'r2', 'roc_auc')
        self.assertEqual(expected, MetricsPossibilities.available_cases())


if __name__ == '__main__':
    unittest.main()
