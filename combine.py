"""
This is a script for combining all flashcards in `sets/` into a single 
flashcard data file: `all.tsv`
"""

import os

def combine(): 
    for set in os.listdir('sets'):
        print(f'Parsing set: {set}')

if __name__ == '__main__': 
    combine()