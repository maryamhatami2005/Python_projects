"""
Author: Mary
Date Created: 17/11/2025
Description: Rock Paper Scissors game.
"""

from random import choice
from typing import List, Tuple

class RockPaperScissors:
    def __init__(self, name: str):
        """ Main class for Rock Paper Scissors game."""
        self.choices: List[str] = ["rock", "paper", "scissors"]
        self.player_name: str = name

    def get_player_choice(self) -> str:
        user_choice : str = input(f"Enter your choice({self.choices})")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        else:
            print(f"Invalid choice. You must select from {self.choices}.")
            return self.get_player_choice()
        
    def get_computer_choice(self) -> str:
        """ Get computer choicr randomly from choices: rock, paper, scissors."""
        return choice(self.choices)
    
    def decide_winner(self, user_choice: str, computer_choice: str) -> str:
        """ Decide the winner of the game based on user and computer choices.

        :param user_choice: The choice of user
        :param computer_choice: The choice of computer
        :return: The result of the game. {who won the game}
        """
        if user_choice == computer_choice:
            return "It's a Tie\n"
        win_combinations: List[Tuple[str, str]] = [('rock', 'scissors'), ('paper', 'rock'), ('rock', 'paper')]
        for win_comb in win_combinations:
            if (user_choice == win_comb[0]) and (computer_choice == win_comb[1]):
                return "Congrats! You Won\n"
            else:
                return "Oh no! The computer won\n"

    def play(self):
        """Play the game.
        - Get user choice.
        - Get computer choice.
        - Decide the winner.
        - Print the winner.
        """
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(f"Computer choice: {computer_choice}")
        print(winner_msg)



if __name__ == "__main__":
    game = RockPaperScissors("Mary")

    while True:
        game.play()
        continue_game = input("Do you want to play again? (Enter any key to play again, enter q to exit.): ")
        if continue_game.lower() == "q":
            break