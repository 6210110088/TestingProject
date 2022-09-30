from gridchallenge.gridchallenge_utils import *
import unittest

class GridChallengeTest(unittest.TestCase):
    def test_give_eabcd_fghij_olkmn_trpqs_xywuv_is_YES(self):
        grid = ['eabcd','fghij','olkmn','trpqs','xywuv']
        expected_result = 'YES'
        result = gridChallenge(grid)
        self.assertEqual(result, expected_result)