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

    def test_give_1_3_2_should_be_MouseC(self):
        var_x = 1
        var_y = 3
        var_z = 2
        expected_output = 'Mouse C'
        result = cat_mouse(var_x, var_y, var_z)
        self.assertEqual(result, expected_output)

    def test_give_5_9_6_should_be_CatA(self):
        var_x = 5
        var_y = 9
        var_z = 6
        expected_output = 'Cat A'
        result = cat_mouse(var_x, var_y, var_z)
        self.assertEqual(result, expected_output)

    def test_give_0_0_0_should_be_None(self):
        var_x = 0
        var_y = 0
        var_z = 0
        expected_output = None
        result = cat_mouse(var_x, var_y, var_z)
        self.assertIsNone(result, expected_output)