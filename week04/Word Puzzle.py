"""Word guessing game.
This game challenges the player to guess a hidden word by using clues after every attempt.
The player receives feedback on each letter to help narrow down the correct answer.
"""

import random

# List of possible secret words
words = ["christ", "michael", "daniel", "victor", "andrea", "gabriel"]

# Randomly choose a secret word
secret_word = random.choice(words)

# Create the initial hint with underscores and spaces
hint = ["_"] * len(secret_word)

print("Welcome to the Word Guessing Game!")
print("Try to guess the secret word. Each guess must be the same length as the hidden word.")
print("Your hint is:", " ".join(hint))

guesses = 0

while True:
    guess = input("What is your guess? ").strip().lower()
    guesses += 1

    # Check guess length
    if len(guess) != len(secret_word):
        print(f"Sorry, your guess must have exactly {len(secret_word)} letters.")
        continue

    # Check if the guess is correct
    if guess == secret_word:
        print(f"Congratulations! You guessed the secret word: {secret_word}")
        print(f"It took you {guesses} guesses.")
        break

    # Generate a clue for this guess
    new_hint = []

    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            new_hint.append(guess[i].upper())
        elif guess[i] in secret_word:
            new_hint.append(guess[i].lower())
        else:
            new_hint.append("_")

    print("Your hint is:", " ".join(new_hint))
    print("_ = letter not in the word")
    print("lowercase = letter is in the word but not in this position")
    print("uppercase = letter matches this exact position")