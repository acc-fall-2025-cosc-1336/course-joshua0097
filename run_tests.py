import unittest

# The test functions are now located in src/tests/homework/d_repetition/test_repetition.py

from tests.homework.d_repetition import tests_repetition

suite = unittest.TestLoader().loadTestsFromModule(tests_repetition)
unittest.TextTestRunner(verbosity=2).run(suite)

# updated run_tests.py for homework 4