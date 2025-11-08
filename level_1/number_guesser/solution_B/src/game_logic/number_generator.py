import random

def generate_random_number(start: int, end: int) -> int:
    """ 
    Generates a random number number between start and end.
    """
    return random.randint(start, end)