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

    def test_give_AlwaysLookontheBrightSideofLife_5_is_FqbfdxQttptsymjGwnlmyXnijtkQnkj(self):
        text = 'Always-Look-on-the-Bright-Side-of-Life'
        rotate = 5
        expected_result = 'Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj'
        result = caesarCipher(text, rotate)
        self.assertEqual(result, expected_result)
        
    def test_give_Theresastarmanwaitinginthesky_3_is_Wkhuhvdvwdupdqzdlwlqjlqwkhvnb(self):
        text = 'There\'s-a-starman-waiting-in-the-sky'
        rotate = 5
        expected_result = 'Wkhuh\'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb'
        result = caesarCipher(text, rotate)
        self.assertEqual(result, expected_result)