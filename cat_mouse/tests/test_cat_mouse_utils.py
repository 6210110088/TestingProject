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

    def test_give_0_5_6_should_be_None(self):
        var_x = 0
        var_y = 5
        var_z = 6
        expected_output = None
        result = cat_mouse(var_x, var_y, var_z)
        self.assertIsNone(result, expected_output)

    def test_give_33_86_59_should_be_CatA(self):
        var_x = 33
        var_y = 86
        var_z = 59
        expected_output = 'Cat A'
        result = cat_mouse(var_x, var_y, var_z)
        self.assertEqual(result, expected_output)

    def test_give_22_75_70_should_be_CatB(self):
        var_x = 22
        var_y = 75
        var_z = 70
        expected_output = 'Cat B'
        result = cat_mouse(var_x, var_y, var_z)
        self.assertEqual(result, expected_output)

    def test_give_21_95_58_should_be_MouseC(self):
        var_x = 21
        var_y = 95
        var_z = 58
        expected_output = 'Mouse C'
        result = cat_mouse(var_x, var_y, var_z)
        self.assertEqual(result, expected_output)