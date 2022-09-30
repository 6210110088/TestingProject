from funnystring.funnystring_utils import *
import unittest
from unittest import mock

class FunnyStringTest(unittest.TestCase):
    def test_give_acxz_is_funny(self):
        text = 'acxz'
        expected_result = 'Funny'
        result = funnyString(text)
        self.assertEqual(result, expected_result)

    def test_give_bcxz_is_notfunny(self):
        text = 'bcxz'
        expected_result = 'Not Funny'
        result = funnyString(text)
        self.assertEqual(result, expected_result)

    def test_give_ivvkxq_is_notfunny(self):
        text = 'ivvkxq'
        expected_result = 'Not Funny'
        result = funnyString(text)
        self.assertEqual(result, expected_result)

    def test_give_ivvkx_is_notfunny(self):
        text = 'ivvkx'
        expected_result = 'Not Funny'
        result = funnyString(text)
        self.assertEqual(result, expected_result)