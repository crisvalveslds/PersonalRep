import random

play_again = ""

while play_again != "n":
    number = random.randint(1, 100)
    tries = 0
    guess = 0
    play_again = ""

    while guess != number:
        tries += 1
        guess = int(input("Guess a number between 1 and 100: "))
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")

    print(f"You guessed it right! The number was {number}. It took you {tries} tries.")
    print("")
    play_again = input("Do you want to play again? (y/n): ")

print("Thanks for playing!")