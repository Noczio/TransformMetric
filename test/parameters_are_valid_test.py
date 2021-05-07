import unittest
from resources.concrete.sys_data import SysParameterValidator


class MyTestCase(unittest.TestCase):
    def test_are_valid_1(self):
        validator = SysParameterValidator(debug=True)
        parameters = ("roc_auc", "1", "0", "0.5")
        are_valid = validator.parameters_are_valid(*parameters)
        self.assertTrue(are_valid)

    def test_are_valid_2(self):
        validator = SysParameterValidator(debug=True)
        parameters = ("roc_auc", 1, "0", "0.5")
        are_valid = validator.parameters_are_valid(*parameters)
        self.assertTrue(are_valid)

    def test_are_valid_3(self):
        validator = SysParameterValidator(debug=True)
        parameters = ("roc_auc", 0.676)
        are_valid = validator.parameters_are_valid(*parameters)
        self.assertTrue(are_valid)

    def test_are_not_valid_1(self):
        validator = SysParameterValidator(debug=True)
        parameters = ("roc_auc", "s", "-3", "0.5")
        are_valid = validator.parameters_are_valid(*parameters)
        self.assertFalse(are_valid)

    def test_are_not_valid_2(self):
        validator = SysParameterValidator(debug=True)
        parameters = ("roc", 1, 0)
        are_valid = validator.parameters_are_valid(*parameters)
        self.assertFalse(are_valid)

    def test_are_not_valid_3(self):
        validator = SysParameterValidator(debug=True)
        parameters = ("roc_auc", "-1")
        are_valid = validator.parameters_are_valid(*parameters)
        self.assertFalse(are_valid)


if __name__ == '__main__':
    unittest.main()
