# lib/anagram.py

class Anagram:
    def __init__(self, word):
        """
        Initialize with a word that the class will use to find anagrams.
        """
        self.word = word.lower()

    def match(self, word_list):
        """
        Takes a list of possible anagrams and returns a list of matches.
        """
        # Sort the letters of the base word for comparison
        sorted_word = sorted(self.word)
        
        # Find words in the list that are anagrams
        return [w for w in word_list if sorted(w.lower()) == sorted_word]
