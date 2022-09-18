from fizzbuzz.fizzbuzz_utils import fizzbuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        number = 3
        expected_result = 'Fizz'
        result = fizzbuzz(number)
        self.assertEqual(result, expected_result)

    def test_give_5_is_buzz(self):
        number = 5
        expected_result = 'Buzz'
        result = fizzbuzz(number)
        self.assertEqual(result, expected_result)

    def test_give_15_is_fizzbuzz(self):
        number = 15
        expected_result = 'FizzBuzz'
        result = fizzbuzz(number)
        self.assertEqual(result, expected_result)