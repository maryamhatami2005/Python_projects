def provide_hint(guess, actual_number):
    if guess < actual_number:
        return "Try a higher number."
    elif guess > actual_number:
        return "Try a lower number."
