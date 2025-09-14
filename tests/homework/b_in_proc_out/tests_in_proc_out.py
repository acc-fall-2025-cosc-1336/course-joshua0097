import unittest

from src.homework.b_in_proc_out.output import get_meal_amount, get_sales_tax_amount, get_tip_amount

class Test_Config(unittest.TestCase):

    def test_get_meal_amount(self):
        # Test that the function get_meal_amount returns a float
        self.assertIsInstance(get_meal_amount(), float)

    def test_get_sales_tax_amount(self):
        # Test that the function get_sales_tax_amount returns the correct sales tax
        self.assertEqual(get_sales_tax_amount(100, 0.0675), 6.75)

    def test_get_tip_amount(self):
        # Test that the function get_tip_amount returns the correct tip
        self.assertEqual(get_tip_amount(100, 0.15), 15.0)
        self.assertEqual(get_tip_amount(50, 0.20), 10.0)

