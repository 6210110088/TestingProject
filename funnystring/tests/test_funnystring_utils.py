from funnystring.funnystring_utils import *
import unittest

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_is_funny(self):
        text = 'acxz'
        expected_result = 'Funny'
        result = funnyString(text)
        self.assertEqual(result, expected_result)

    def test_give_bcxz_is_funny(self):
        text = 'bcxz'
        expected_result = 'Not Funny'
        result = funnyString(text)
        self.assertEqual(result, expected_result)