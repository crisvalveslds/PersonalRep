# Guessing word game
# It was really interesting to learn how to build such a game using loops
# I had to research a few things that were not on the initial material, 
# like joining list's components into a single string with .join(), 
# or using random.choice() to select one word between all the words stored in the list

import random

mixed_words = [
    "apple", "banana", "orange", "grape", "mango",
    "tiger", "lion", "zebra", "panther", "falcon",
    "ocean", "forest", "desert", "island", "village",
    "city", "harbor", "mountain", "canyon", "meadow",
    "python", "variable", "function", "integer", "boolean",
    "storm", "thunder", "rainbow", "horizon", "galaxy",
    "silver", "granite", "marble", "quartz", "crystal",
    "future", "victory", "destiny", "journey", "memory",
    "panda", "kangaroo", "dolphin", "leopard", "ostrich",
    "peach", "pear", "kiwi", "fig", "papaya",
    "brazil", "america", "vietnam", "japan", "egypt",
    "castle", "temple", "airport", "station", "harvest",
    "nebula", "cosmos", "asteroid", "comet", "supernova",
    "lighthouse", "waterfall", "glacier", "tundra", "savanna",
    "courage", "harmony", "freedom", "whisper", "shadow",
    "photon", "quantum", "entropy", "momentum", "inertia",
    "labyrinth", "paradox", "enigma", "obsidian", "mythical",
    "sapphire", "emerald", "topaz", "onyx", "amethyst",
    "avalanche", "tsunami", "volcano", "hurricane", "cyclone",
    "compassion", "reflection", "solitude", "wanderlust", "evermore"
]

play_again = ""

print("Welcome to Guessing Game!")

while play_again != "n":
    word = random.choice(mixed_words)
    tries = 0
    guess = ""
    size = len(word)
    guessing = ["_"] * size
    guessed = []

    print(f"This is our word: {" ".join(guessing)}")
    print("Now it is your turn!")

    while "".join(guessing) != word:
        guessing = ["_"] * size
        tries += 1
        guess = input("Guess a word: ").lower()
        
        if guess == word:
            break
        
        if len(guess) != size:
            print("Your guess must have the same number of letters as the word!")
            continue

        if guess in guessed:
            print("You already guessed that word!")
            continue
        
        guessed.append(guess)
        
        for i in range(size):
            for j in range(size):
                if guess[i] == word[j]:
                    if i == j:
                        guessing[i] = guess[i].upper()
                        break
                    else:
                        guessing[i] = guess[i].lower()
                        break

        print(f"Here is a hint: {" ".join(guessing)}")
        
    print(f"You guessed it right! The word was {word.upper()}. It took you {tries} tries.")
    print("")
    play_again = input("Do you want to play again? (y/n): ")

print("Thanks for playing!")