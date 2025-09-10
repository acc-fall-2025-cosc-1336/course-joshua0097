import unittest

from src.homework.b_in_proc_out.output import multiply_numbers

class Test_Config(unittest.TestCase):

    def test_multiply_numbers(self):
        # Test that the function multiply_numbers returns the product of two numbers
        self.assertEqual(multiply_numbers(1, 1), 1)
        self.assertEqual(multiply_numbers(2, 2), 4)
        self.assertEqual(multiply_numbers(2, 3), 6)

