import random

class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def guess(self, number):
        self.attempts += 1
        if number == self.secret_number:
            return True
        return False
