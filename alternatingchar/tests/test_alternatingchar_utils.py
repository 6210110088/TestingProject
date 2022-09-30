from alternatingchar.alternatingchar_utils import *
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_give_aaaa_is_3(self):
        text = 'aaaa'
        expected_result = 3
        result = alternatingCharacters(text)
        self.assertEqual(result, expected_result)

    def test_give_bbbbb_is_4(self):
        text = 'bbbbb'
        expected_result = 4
        result = alternatingCharacters(text)
        self.assertEqual(result, expected_result)

    def test_give_abababab_is_0(self):
        text = 'abababab'
        expected_result = 0
        result = alternatingCharacters(text)
        self.assertEqual(result, expected_result)

    def test_give_bababa_is_0(self):
        text = 'bababa'
        expected_result = 0
        result = alternatingCharacters(text)
        self.assertEqual(result, expected_result)

    def test_give_aaabbb_is_4(self):
        text = 'aaabbb'
        expected_result = 4
        result = alternatingCharacters(text)
        self.assertEqual(result, expected_result)