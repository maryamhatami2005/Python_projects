import random

def validate_input(user_num):
    if not user_num.isdigit():
        print("Invalid input, please try again.")
        return False

    user_num = int(user_num)
    if user_num > 100 or user_num < 1:
        print("You are out of range.Your guess should be between 1 and 100.")
        return False
    
    return True


def main():
    score = 100
    rand_num = random.randint(0,100)

    while True:
        user_guess = input("Guess a number between 1 and 100: ")
        if user_guess =="q":
            print("Thank you for playing. Goodbye!")
            break
        
        if not validate_input(user_guess):
            continue

        user_guess = int(user_guess)
        if rand_num > user_guess:
            print("Your guess is too low. Please try again.")

        elif rand_num < user_guess:
            print("Your guess is too high. Pleas try again.")
        if rand_num == user_guess:
            print (f"Congratulations! You guessed correctly. Your score is: {score}")
            wanna_play = input("DO you want to play again? (y/n)")
            if wanna_play == 'y':
                score = 100
                rand_num = random.randint(0,100)
                continue
            elif wanna_play == 'n':
                print("Goodbye!")
                break

        score -= 10
        score = max(score, 0)


if __name__ == "__main__":
    main()
