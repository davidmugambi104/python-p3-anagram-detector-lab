# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        sorted_word = sorted(self.word)
        return [word for word in words if sorted(word) == sorted_word]

    