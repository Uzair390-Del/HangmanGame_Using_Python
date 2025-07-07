# 1: words.txt
import random

# load words from the file
def load_words(filename):
    try:
        with open(filename,mode='r') as file:
            words= file.read().splitlines()
            if not words:
                print("The word list is empty. Please add words to the  file.")
            return words
    except FileNotFoundError:
        print("Word file not found! please the file is present or not!")
        return []