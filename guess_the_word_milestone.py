# Guessing word game
import random

mixed_words = [
    "apple", "banana", "orange", "grape", "mango"
]

play_again = ""

print("Welcome to Guessing Game!")

while play_again != "n":
    word = random.choice(mixed_words)
    tries = 0
    guess = ""
    
    while guess != word:
        tries += 1
        guess = input("Guess a word: ").lower()
        if guess != word:
            print("Wrong guess!")
        
    print(f"You guessed it right! The word was {word.upper()}. It took you {tries} tries.")
    print("")
    play_again = input("Do you want to play again? (y/n): ")

print("Thanks for playing!")