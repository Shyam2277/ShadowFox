# hangman code (reverse hangman)
# *rules* 
# -A player has to guess a word by guessing random letters (no numbers or any symbols)
# -if the letter is in the word, then the blank is filled with the correct letter at its position
# -if the letter is wrong, then a part of the hangman is drawn (head, arms, legs etc)
# -if a player guesses the word before the hangman is drawn, he/she wins otherwise if the hangman is fully drawn, then the player loses

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

def get_word():
    try:
        with open('/Users/shyamsindhu/Documents/internship work/codes/Task 2/hangman game words.txt', 'r') as f:
            words = f.read().splitlines()
        return random.choice(words)
    except FileNotFoundError:
        print("Error: the file path was not found.")
        exit()

def hangman():
    chosen_word = get_word()
    display = ["_" for _ in chosen_word]
    guessed_letters = set()  # To track guessed letters
    lives = 6

    print("\n------------- Welcome to Hangman -------------\n")
    print("Guess the word: ", " ".join(display))
    print("Lives:", lives, "\n")
    
    while lives > 0:
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed '" + guess + "'. Try another letter.")
            continue

        # Add guess to the set of guessed letters
        guessed_letters.add(guess)

        # Process the guess
        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = guess
            print("\nCorrect!")
        else:
            lives -= 1
            print("\nWrong!")

        # Show the current game status
        print(" ".join(display))
        print("Lives:", lives)
        print(stages[6 - lives])

        # Check win condition
        if "_" not in display:
            print("\nCongratulations! You guessed the word! It was : ", chosen_word)
            return

    print("\nYou lost! The word was:     " + chosen_word)

# Main game loop
while True:
    play = input("Do you want to play Hangman? (y/n): ").lower()
    if play in ['y', 'yes']:
        hangman()
    elif play in ['n', 'no']:
        print("Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

