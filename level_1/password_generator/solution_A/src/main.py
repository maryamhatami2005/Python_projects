import random
import string
from abc import ABC, abstractmethod
from typing import List, Optional

import nltk

nltk.download("words")

class PasswordGenerator(ABC):
    """ Base class for generating passwords.
    """
    @abstractmethod
    def generate(self) -> str:
        pass

class PinGenerator(PasswordGenerator):
    """ Class to generate a numeric pin code.
    """
    def __init__(self, length: int):
        self.length: int = length

    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for n in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    """ Class to generate a random password.
    """
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation


    def generate(self) -> str:
        return ''.join(random.choice(self.characters) for n in range(self.length))
    

class MemorablePasswordGenerator(PasswordGenerator):
    """ Class to generate a memorable password.
    """
    def __init__(
        self, number_of_words: int = 4,
        seprator: str = '-',
        upper: bool = True,
        vocabulary:  Optional[List[str]] = None):

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.number_of_words: int = number_of_words
        self.upper: bool = upper
        self.seprator: str = seprator
        self.vocabulary: List[str] = vocabulary

    def generate(self) -> str:
        password_words = [random.choice(self.vocabulary) for n in range(self.number_of_words)]
        if self.upper:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        return self.seprator.join(password_words)
    

if __name__ == "__main__":

    memorable_pass = MemorablePasswordGenerator()
    print(memorable_pass.generate())

    pin = PinGenerator(4)
    print(pin.generate())

    random_pass = RandomPasswordGenerator()
    print(random_pass.generate())