from random import choice


class RockPaperScissors:
    def __init__(self, name: str, rounds: int):
        """ Main clsass for Rock Paper Scissors game.
        :param name: Gets player's name
        :param rounds: Gets how many rounds does user wants to paly
        """
        self.user_name = name.title()
        self.rounds = rounds
        self.options = ["rock", "paper", "scissors"]
        self.computer_score = 0
        self.user_score = 0

    def get_computer_choice(self) -> str:
        """ Get computer choice randomly from choices: rock, paper, scissors."""
        return choice(self.options)

    def get_user_choice(self) -> str:
        user_choice = input("Choose from rock/paper/scissors: ")
        if user_choice.lower() in self.options:
            return user_choice.lower()
        else:
            print("You must choose from rock/paper/scissors")
            return self.get_user_choice()
        
    def score(self, user_choice, computer_choice):
        """Compare user and computer choices and update their scores."""
        if user_choice == computer_choice:
            return "It's a Tie. Try one more time"
        
        if computer_choice == "rock":
            if user_choice == "paper":
                self.user_score += 1
            else:
                self.computer_score +=1
        
        if computer_choice == "paper":
            if user_choice == "scissors":
                self.user_score +=1
            else:
                self.computer_score +=1

        if computer_choice == "scissors":
            if user_choice == "rock":
                self.user_score += 1
            else:
                self.computer_score += 1
    
    def winner(self):
        """ Compares user and computer scores after all rounds and prints the winner accordingly."""
        if self.user_score == self.computer_score:
            print(f"Computer's score: {self.computer_score}")
            print (f"{self.user_name}'s score: {self.user_score}")
            print("It's a Tie")
        elif self.user_score > self.computer_score:
            print(f"Computer's score: {self.computer_score}")
            print (f"{self.user_name}'s score: {self.user_score}")
            print("Congrats! You won.")
        else:
            print(f"Computer's score: {self.computer_score}")
            print (f"{self.user_name}'s score: {self.user_score}")
            print("Oh no! The computer won.")

    def game(self):
        """For each round:
        - Get the computer's choice.
        - Get the user's choice.
        - Update the score.
        - Decide the winner.
        """
        for n in range(1, self.rounds + 1):
            computer = self.get_computer_choice()
            user = self.get_user_choice()
            print(f"Computer chose: {computer}")
            print(f"{self.user_name} chose: {user} \n")
            self.score(user, computer)
        self.winner()

if __name__ =="__main__": 
    user_name = input("Please Enter your name: ")
    rounds = int(input("How many rounds do you want to play? "))
    play_game = RockPaperScissors(user_name, rounds)
    play_game.game()


