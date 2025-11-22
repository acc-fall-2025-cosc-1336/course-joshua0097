import unittest

# The test functions are now located in src/tests/homework/i_dictionaries_sets/tests_dictionaries_and_sets.py

from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets

suite = unittest.TestLoader().loadTestsFromModule(tests_dictionaries_and_sets)
unittest.TextTestRunner(verbosity=2).run(suite)

# updated run_tests.py for homework 9