from random import choice
import nltk
import string
from typing import List


def generate_pin_code(length:int = 4) -> str:
    """ Generate a numeric pin code.
    """
    return "".join([choice(string.digits) for n in range(length)])


def generate_random_password(length: int = 8, include_nums: bool = True, include_symbols: bool = True) -> str:
    """ Generate a random password.
    """
    characters = string.ascii_letters
    if include_nums:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    return "".join([choice(characters) for n in range(10)])


def generate_memorable_password(length: int = 4,seprator: str = "-",upper: bool = True, vocabluary: List[str] = None) -> str:
    """ Generate a memorable password from a list of vocabulary words.
    """
    if vocabluary is None:
        vocabluary = nltk.corpus.words.words()
    password_words =  [choice(vocabluary) for n in range(length)]
    
    if upper:
        password_words = [word.upper() if choice([True ,False]) else word.lower() for word in password_words]
    return seprator.join(password_words)

def main():
    pin = generate_pin_code()
    print(pin)

    random = generate_random_password()
    print(random)

    memorable = generate_memorable_password()
    print(memorable)

if __name__ == "__main__":
    main()
