from twochar.twochar_utils import *
import unittest

class TwoCharTest(unittest.TestCase):
    def test_give_beabeefeab_is_5(self):
        text = 'beabeefeab'
        expected_result = 5
        result = alternate(text)
        self.assertEqual(result, expected_result)

    def test_give_asdcbsdcagfsdbgdfanfghbsfdab_is_8(self):
        text = 'asdcbsdcagfsdbgdfanfghbsfdab'
        expected_result = 8
        result = alternate(text)
        self.assertEqual(result, expected_result)

    def test_give_asvkugfiugsalddlasguifgukvsa_is_0(self):
        text = 'asvkugfiugsalddlasguifgukvsa'
        expected_result = 0
        result = alternate(text)
        self.assertEqual(result, expected_result)

    def test_give_a_is_0(self):
        text = 'a'
        expected_result = 0
        result = alternate(text)
        self.assertEqual(result, expected_result)

    def test_give_cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc_is_8(self):
        text = 'cwomzxmuelmangtosqkgfdqvkzdnxerhravxndvomhbokqmvsfcaddgxgwtpgpqrmeoxvkkjunkbjeyteccpugbkvhljxsshpoymkryydtmfhaogepvbwmypeiqumcibjskmsrpllgbvc'
        expected_result = 8
        result = alternate(text)
        self.assertEqual(result, expected_result)

    def test_give_ab_is_2(self):
        text = 'ab'
        expected_result = 2
        result = alternate(text)
        self.assertEqual(result, expected_result)

    def test_give_aaaa_is_0(self):
        text = 'aaaa'
        expected_result = 0
        result = alternate(text)
        self.assertEqual(result, expected_result)