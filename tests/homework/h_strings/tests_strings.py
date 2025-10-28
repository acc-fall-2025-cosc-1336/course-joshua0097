import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):

    def test_get_hamming_distance(self):
        s1 = "GAGCCTACTAACGGGAT"
        s2 = "CATCGTAATGACGGCCT"
        self.assertEqual(get_hamming_distance(s1, s2), 7)

    def test_get_dna_complement(self):
        s = "AAAACCCGGT"
        self.assertEqual(get_dna_complement(s), "ACCGGGTTTT")

if __name__ == "__main__":
    unittest.main()