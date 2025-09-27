import unittest
'''
the file in src/tests/homework/d_repetition/tests_repetition.py
has the test functions
'''
from tests.homework.d_repetition import tests_repetition 

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)

#both functions are tested in tests_repetition.py