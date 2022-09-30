from re import X
from cat_mouse.cat_mouse_utils import *
import unittest

class CatandMouseTest(unittest.TestCase):
    def test_give_1_2_3_should_be_CatB(self):
        var_x = 1
        var_y = 2
        var_z = 3
        expected_output = 'Cat B'
        result = cat_mouse(var_x, var_y, var_z)
        self.assertEqual(result, expected_output)