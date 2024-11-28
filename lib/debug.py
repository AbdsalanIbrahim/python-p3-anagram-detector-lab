# lib/debug.py

from anagram import Anagram

if __name__ == '__main__':
    # Test cases
    listen = Anagram("listen")
    print(listen.match(["enlists", "google", "inlets", "banana"]))  # Expected: ['inlets']

    another = Anagram("enlist")
    print(another.match(["listen", "silent", "hippopotamus"]))  # Expected: ['listen', 'silent']
