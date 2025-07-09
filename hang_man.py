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
# hangman game logic
def play_hangman(words):
    word= random.choice(words).lower()
    guessed_word=["-"]*len(word)
    # eg if python then "_ _ _ _ _ _"
    attempts= 6
    guessed_letters= set()
    print("Welcome to the hangman!")
    print("Guess the word by entering one letter at a time")
    while attempts>0 and "_" in guessed_word:
        print(f"\n Word:"," " .join(guessed_word))
        print(f"Guesses Left:{attempts}")
        print(f"Guesses letters: {', '.join(sorted(guessed_letters))}")
        guess= input("Guess a letter : ").lower()
        if len(guess) !=1 or not guess.isalpha():
            print("Invalid Inputs. please enter a single alphabetical number!")
            continue
        if guess in guessed_letters:
            print("You already guessed that latter!")
        elif guess in word:
            print("correct!")
            for i, letter in guessed_letters:
                print("You already guessed that letter!")
                # if i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i]==guess
            guessed+letters.add(guess)
        else:
            print("Incorrect!")
            attempts-=1
            guessed_letters.add(guess)
        if "_" not in guessed_word:
            print(f"\n Congratulations! you guessed the word: {word}")
        else:
            print(f"\n Game over! the word was: {word}")
def main():
    print("Hangma Game")
    words= load_words('words.txt')
    if not words:
        return
    while True:
        play_hangman(words)
        replay= input("\n Do you want to play again? (yes/no):")
        if replay not in ("yes","y"):
            print("Thanks For playing! GoofBye!")
            break
if __name__=="__main__":
    main()
                    