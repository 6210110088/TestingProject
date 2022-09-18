class SuperFizzBuzz:
    def __init__(self, num: int):
        self.num = num

    def check(self):
        pass

class Fizz(SuperFizzBuzz):
    def check(self):
        if self.num%3 == 0:
            return 'Fizz'
        else:
            return None

class Buzz(SuperFizzBuzz):
    def check(self):
        if self.num%5 == 0:
            return 'Buzz'
        else:
            return None

class FizzFizz(SuperFizzBuzz):
    def check(self):
        if self.num%9 == 0:
            return 'FizzFizz'
        else:
            return None

class BuzzBuzz(SuperFizzBuzz):
    def check(self):
        if self.num%25 == 0:
            return 'BuzzBuzz'
        else:
            return None

class FizzBuzz(SuperFizzBuzz):
    def check(self):
        if self.num%3 == 0 and self.num%5 == 0:
            return 'FizzBuzz'
        else:
            return None

class FizzFizzBuzzBuzz(SuperFizzBuzz):
    def check(self):
        if self.num%9 == 0 and self.num%25 == 0:
            return 'FizzFizzBuzzBuzz'
        else:
            return None

def checkfizzbuzz(num: int):
    conditions = [
        Fizz(num),
        Buzz(num),
        FizzBuzz(num),
        FizzFizz(num),
        BuzzBuzz(num),
        FizzFizzBuzzBuzz(num),
        SuperFizzBuzz(num),
    ]

    result = ''

    for condition in conditions:
        if condition.check() != None:
            result = condition.check()

    if result == '':
        result = 'NoFizzBuzz'

    return result