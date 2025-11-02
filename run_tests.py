import unittest

# The test functions are now located in src/tests/homework/g_lists_and_tuples/tests_lists_and_tuples.py

from tests.homework.g_lists_and_tuples import tests_lists_and_tuples

suite = unittest.TestLoader().loadTestsFromModule(tests_lists_and_tuples)
unittest.TextTestRunner(verbosity=2).run(suite)

# updated run_tests.py for homework 7