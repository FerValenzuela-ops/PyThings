
import main
import unittest

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = ('@@@23112', 2)
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, (ValueError, TypeError))

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')

if __name__ == '__main__':
  unittest.main()