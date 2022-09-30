from twochar.twochar_utils import *
import unittest

class TwoCharTest(unittest.TestCase):
    def test_give_beabeefeab_is_5(self):
        text = 'beabeefeab'
        expected_result = 5
        result = alternate(text)
        self.assertEqual(result, expected_result)