import random


class NumberGuessing:
    def __init__(self, min_number, max_number) -> None:
        self.max_number = max_number
        self.min_number = min_number

    @classmethod
    def guess(cls, min_number=1, max_number=100):
        return cls(min_number, max_number)

    def play(self):
        random_number = random.randint(self.min_number, self.max_number)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between {self.min_number} and {self.max_number} "))
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        print(f"Yay, congrats. You have guessed the number {random_number} correctly ! .")