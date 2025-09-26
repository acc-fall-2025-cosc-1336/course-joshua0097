import unittest

from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio

class Test_Config(unittest.TestCase):

    def test_get_faculty_rating(self):
        self.assertEqual(get_faculty_rating(0.5), "Unacceptable")
        self.assertEqual(get_faculty_rating(0.65), "Needs Improvement")
        self.assertEqual(get_faculty_rating(0.75), "Good")
        self.assertEqual(get_faculty_rating(0.85), "Very Good")
        self.assertEqual(get_faculty_rating(0.95), "Excellent")
        self.assertEqual(get_faculty_rating(1.1), "Invalid Ratio")

    def test_get_options_ratio(self):
        self.assertAlmostEqual(get_options_ratio(50, 100), 0.5)
        self.assertAlmostEqual(get_options_ratio(70, 100), 0.7)
        self.assertAlmostEqual(get_options_ratio(80, 100), 0.8)
        self.assertAlmostEqual(get_options_ratio(90, 100), 0.9)
        self.assertAlmostEqual(get_options_ratio(100, 100), 1.0)
    
