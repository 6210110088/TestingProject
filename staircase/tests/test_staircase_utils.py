from staircase.staircase_utils import *
import unittest

class StairCaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = '#'
        expected_output = [' #', '##']
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_4_with_star_should_be_starstarstarstar(self):
        n = 4
        pattern = '*'
        expected_output = ['   *', '  **', ' ***', '****']
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_1_with_a_should_be_a(self):
        n = 1
        pattern = 'a'
        expected_output = ['a']
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)