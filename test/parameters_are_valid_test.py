import unittest
from resources.concrete.handler.argument_handler import SysArgumentHandler


class MyTestCase(unittest.TestCase):
    def test_are_valid_1(self):
        handler = SysArgumentHandler(debug=True)
        parameters = ("test.py", "completeness_score", "1", "0", "0.5")
        handler.handle_arguments(*parameters)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
