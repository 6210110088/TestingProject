from faulthandler import cancel_dump_traceback_later
from caesarcipher.caesarcipher_utils import *
import unittest

class CaesarCipherTest(unittest.TestCase):
    def test_give_middle_dash_Outz_2_is_okffng_dash_Qwvb(self):
        text = 'middle-Outz'
        rotate = 2
        expected_result = 'okffng-Qwvb'
        result = caesarCipher(text, rotate)
        self.assertEqual(result, expected_result)