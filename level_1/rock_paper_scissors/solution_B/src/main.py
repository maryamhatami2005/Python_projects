from random import choice


choices = ['rock', 'paper', 'scissors']

def get_user_choice() -> str:
    """Gets the user's choice."""
    user_choice = input("Enter your choice (rock, paper, scissors): ")
    if user_choice.lower() in choices :
        return user_choice.lower()
    else:
        print("Invalid input. Choose between rock, paper, and scissors")
        return get_user_choice()


def get_computer_choice() -> str:
    """Gets the computer's choice."""
    return choice(choices)


def winner(user_choice: str, computer_choice: str):
    """Determines the winner."""
    winner_combo = {
        'rock' : 'scissors', 
        'paper' : 'rock',
        'scissors' : 'paper'
    }
    if user_choice == computer_choice:
        return "It's a tie"
    elif winner_combo[user_choice] == computer_choice:
        return 'User wins'
    else:
        return 'Computer wins'


def play():
    """Plays the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()    
    print(f"User chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(winner(user_choice, computer_choice))


if __name__ == "__main__":
    play()