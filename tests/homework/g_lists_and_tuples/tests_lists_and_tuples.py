import unittest
from src.homework.g_lists_and_tuples.lists import get_p_distance
from src.homework.g_lists_and_tuples.lists import get_p_distance_matrix

class Test_Config(unittest.TestCase):

      def test_p_distance(self):
            result = get_p_distance(['T','T','T','C','C','A','T','T','T','A'], ['G','A','T','T','C','A','T','T','T','C'])
            self.assertEqual(result, 0.4)
      
      def test_get_p_distance_matrix(self):
            sequences = [
                  ['T','T','T','C','C','A','T','T','T','A'],
                  ['G','A','T','T','C','A','T','T','T','C'],
                  ['T','T','T','C','C','A','T','T','T','T'],
                  ['G','T','T','C','C','A','T','T','T','A']
            ]
            expected = [
                  [0.0, 0.4, 0.1, 0.1],
                  [0.4, 0.0, 0.4, 0.3],
                  [0.1, 0.4, 0.0, 0.2],
                  [0.1, 0.3, 0.2, 0.0]
            ]
            result = get_p_distance_matrix(sequences)
            self.assertEqual(result, expected)