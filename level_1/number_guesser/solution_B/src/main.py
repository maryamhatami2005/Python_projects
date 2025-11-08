from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.hint_generator import provide_hint
from src.game_logic.scorer import Scorer

def main():
    actual_number = generate_random_number(1,100)
    scorer = Scorer()

    while True:
        user_input = get_valid_input(1,100)
        if user_input == actual_number :
            print(f"You guessed the number correctly. Your score is {scorer.get_score()}")
            break
        else:
            hint = provide_hint(user_input, actual_number)
            print(hint)
            scorer.decrement_score()



if __name__ =="__main__":
    main()