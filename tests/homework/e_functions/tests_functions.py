import unittest
from src.homework.e_functions.value_return import get_gross_pay, get_fica_tax, get_federal_tax

class TestPayrollFunctions(unittest.TestCase):

    def test_get_gross_pay(self):
        self.assertAlmostEqual(get_gross_pay(40, 10), 400)
        self.assertAlmostEqual(get_gross_pay(45, 10), 475)  # 40*10 + 5*15
        self.assertAlmostEqual(get_gross_pay(0, 10), 0)
        self.assertAlmostEqual(get_gross_pay(38, 15), 570)

    def test_get_fica_tax(self):
        self.assertAlmostEqual(get_fica_tax(1000), 76.5)
        self.assertAlmostEqual(get_fica_tax(0), 0)
        self.assertAlmostEqual(get_fica_tax(500), 38.25)

    def test_get_federal_tax(self):
        self.assertAlmostEqual(get_federal_tax(1000), 80)
        self.assertAlmostEqual(get_federal_tax(0), 0)
        self.assertAlmostEqual(get_federal_tax(500), 40)
