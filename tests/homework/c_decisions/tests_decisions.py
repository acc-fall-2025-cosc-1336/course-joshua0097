import unittest

from src.homework.c_decisions.decisions import get_letter_grade_if, get_letter_grade_switch

class Test_Config(unittest.TestCase):

    def test_get_letter_grade_if(self): 
        self.assertEqual(get_letter_grade_if(95), 'A')
        self.assertEqual(get_letter_grade_if(85), 'B')
        self.assertEqual(get_letter_grade_if(75), 'C')
        self.assertEqual(get_letter_grade_if(65), 'D')
        self.assertEqual(get_letter_grade_if(50), 'F')

    def test_get_letter_grade_switch(self): 
        self.assertEqual(get_letter_grade_switch(95), 'A')
        self.assertEqual(get_letter_grade_switch(85), 'B')
        self.assertEqual(get_letter_grade_switch(75), 'C')
        self.assertEqual(get_letter_grade_switch(65), 'D')
        self.assertEqual(get_letter_grade_switch(50), 'F')
