from superfizzbuzz.superfizzbuzz_utils import *
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        num = 3
        expected_result = 'Fizz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_5_is_buzz(self):
        num = 5
        expected_result = 'Buzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)
    
    def test_give_9_is_fizzfizz(self):
        num = 9
        expected_result = 'FizzFizz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_25_is_buzzbuzz(self):
        num = 25
        expected_result = 'BuzzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_15_is_fizzbuzz(self):
        num = 15
        expected_result = 'FizzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_225_is_fizzfizzbuzzbuzz(self):
        num = 225
        expected_result = 'FizzFizzBuzzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_4_is_nofizzbuzz(self):
        num = 4
        expected_result = 'NoFizzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_12_is_fizz(self):
        num = 12
        expected_result = 'Fizz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_10_is_buzz(self):
        num = 10
        expected_result = 'Buzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_27_is_fizzfizz(self):
        num = 27
        expected_result = 'FizzFizz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_125_is_buzzbuzz(self):
        num = 125
        expected_result = 'BuzzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_135_is_fizzfizz(self):
        num = 135
        expected_result = 'FizzFizz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_45_is_fizzfizz(self):
        num = 45
        expected_result = 'FizzFizz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_75_is_buzzbuzz(self):
        num = 75
        expected_result = 'BuzzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_375_is_buzzbuzz(self):
        num = 375
        expected_result = 'BuzzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)

    def test_give_3375_is_fizzfizzbuzzbuzz(self):
        num = 3375
        expected_result = 'FizzFizzBuzzBuzz'
        result = checkfizzbuzz(num)
        self.assertEqual(result, expected_result)