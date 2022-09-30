from alternatingchar.alternatingchar_utils import *
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_give_aaaa_is_3(self):
        text = 'aaaa'
        expected_result = 3
        result = alternatingCharacters(text)
        self.assertEqual(result, expected_result)