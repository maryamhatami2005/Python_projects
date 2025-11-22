import random
import string
from abc import ABC, abstractmethod

import nltk

nltk.download("words")

class PasswordGenerator(ABC):
    @abstractmethod
    def generate(self):
        pass

class PinGenerator(PasswordGenerator):
    def __init__(self, length: int):
        self.length = length

    def generate(self) -> str:
        return ''.join([random.choice(string.digits) for n in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.include_numbers = include_numbers
        self.include_symbols = include_symbols
        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation


    def generate(self) -> str:
        return "".join([random.choice(self.characters) for n in range(self.length)])
    

class MemorablePasswordGenerator(PasswordGenerator):
    def __init__(
        self, number_of_words: int = 4,
        seprator: str = '-',
        upper: bool = True,
        vocabulary: list = None):

        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()

        self.number_of_words = number_of_words
        self.upper = upper
        self.seprator = seprator
        self.vocabulary = vocabulary

    def generate(self):
        password_words = [random.choice(self.vocabulary) for n in range(self.number_of_words)]
        if self.upper:
            password_words = [word.upper() if random.choice([True, False]) else word.lower() for word in password_words]
        return self.seprator.join(password_words)
    

if __name__ == "__main__":
    p_obj = RandomPasswordGenerator()
    print(p_obj.generate())

    memorable_pass = MemorablePasswordGenerator()
    print(memorable_pass.generate())