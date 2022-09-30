from staircase.staircase_utils import *
import unittest

class StairCaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = '#'
        expected_output = [' #', '##']
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)