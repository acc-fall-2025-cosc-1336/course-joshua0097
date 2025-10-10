import unittest

# The test functions are now located in src/tests/homework/e_functions/test_functions.py

from tests.homework.e_functions import tests_functions

suite = unittest.TestLoader().loadTestsFromModule(tests_functions)
unittest.TextTestRunner(verbosity=2).run(suite)

# updated run_tests.py for homework 5