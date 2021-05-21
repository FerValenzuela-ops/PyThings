
import main
import unittest

# class TestMain(unittest.TestCase):
#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 15)

#     def test_do_stuff2(self):
#         test_param = ('@@@23112', 2)
#         result = main.do_stuff(test_param)
#         self.assertIsInstance(result, (ValueError, TypeError))

#     def test_do_stuff3(self):
#         test_param = None
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 'Please enter a number')


class TestGame(unittest.TestCase):
    def test_input_correct(self):
        result = main.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.run_guess(0, 11)
        self.assertFalse(result)

    def test_input__wrong_number(self):
        result = main.run_guess(5, 11)
        self.assertFalse(result)   
    def test_input_wrong_type(self):
        result = main.run_guess(5, '11')
        self.assertFalse(result)      


if __name__ == '__main__':
    unittest.main()
