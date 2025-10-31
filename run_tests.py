import unittest

# The test functions are now located in src/tests/homework/h_strings/tests_strings.py

from tests.homework.h_strings import tests_strings

suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)

# updated run_tests.py for homework 6