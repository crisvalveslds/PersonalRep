play_again = ""

while play_again != "n":
    word = input("Type a word: ")
    favorite_letter = input("Type your favorite letter inside that word: ")

    print("Here is the word you typed showing your favorite letter in uppercase: ")

    for letter in word:
        if letter == favorite_letter:
            print(letter.upper(), end="")
        else:
            print(letter.lower(), end="")
    
    print("", end="\n")
    
    play_again = input("Do you want to play again? (y/n): ")

print("Thanks for playing!")