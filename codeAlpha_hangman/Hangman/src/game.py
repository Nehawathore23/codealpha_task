# game.py
import random
from words import WORDS

class Hangman:
    def __init__(self):
        self.word = random.choice(WORDS)
        self.guessed_letters = []
        self.wrong_attempts = 0
        self.max_attempts = 6

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        return display.strip()

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed this letter!")
            return

        self.guessed_letters.append(letter)

        if letter not in self.word:
            self.wrong_attempts += 1
            print("Wrong guess!")
        else:
            print("Correct guess!")

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        return self.wrong_attempts >= self.max_attempts
