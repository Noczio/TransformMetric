import unittest
from resources.concrete.handler.argument_handler import SysArgumentHandler


class MyTestCase(unittest.TestCase):
    def test_are_valid_1(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "completeness_score", "1", "0", "0.5")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_2(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "r2", "-0.78")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_3(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "R2", "1.234")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_4(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "mean_squared_error", "1.234", "0", "-1")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_5(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "Roc_Auc", "1", "0", "0.5", "s", "-1")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_6(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "Accuracy", "1", "0", "0.5", "s", "-1")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_7(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "mutual_info_score", "1", "0", "0.5", "s", "-1", "340")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_8(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "neg_mean_squared_error", "1", "0", "0.5", "s", "-1", "340")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_are_valid_9(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "explained_variance", "1", "0", "0.5", "s", "-1", "340", -345)
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            handler = SysArgumentHandler(debug=False)
            parameters = ("test.py", "mutual_info_score", "1", "0", "0.5", "s", "-1", "340")
            handler.handle_arguments(*parameters)

    def test_not_implemented_metric(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "nonsense", "1", "0", "0.5", "s", "-1", "340")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_2_arguments(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "r2")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)

    def test_1_arguments(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py",)
        handler.handle_arguments(*parameters)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
