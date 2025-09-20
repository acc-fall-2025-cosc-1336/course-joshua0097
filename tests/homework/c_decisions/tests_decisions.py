import unittest

from src.homework.c_decisions.decisions import get_letter_grade

class Test_Config(unittest.TestCase):

    def test_get_letter_grade(self): # tested
        self.assertEqual(get_letter_grade(95), 'A')
        self.assertEqual(get_letter_grade(85), 'B')
        self.assertEqual(get_letter_grade(75), 'C')
        self.assertEqual(get_letter_grade(65), 'D')
        self.assertEqual(get_letter_grade(50), 'F')
         
       
