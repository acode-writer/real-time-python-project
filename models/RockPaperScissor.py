import random


class RockPaperScissor:

    def __init__(self) -> None:
        self.choice = ['r', 'p', 's']

    def play(self):
        # r > s, s > p , p > r
        def is_win(player, opponent): return (player == 'r' and opponent) or (
            player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r')
        user_input = input("What's your choice ? 'r' for rock, 'p' for paper, 's' for scissors ")
        computer_choice = random.choice(self.choice)
        if user_input in self.choice:
            if user_input == computer_choice:
                return "It's a tie"
            if is_win(user_input, computer_choice):
                return f"You won, the computer chose {computer_choice}"
            return f"You lost, the computer chose {computer_choice}"
