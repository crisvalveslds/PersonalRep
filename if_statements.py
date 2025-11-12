first_number = int(input("What is the first number: "))
second_number = int(input("What is the second number: "))

if first_number > second_number:
    print(f"{first_number} is greater than {second_number}.")
    print("Therefore the numbers are not equal.")
    print("And the second number is not greater than the first number.")
elif first_number < second_number:
    print(f"{first_number} is not greater than {second_number}.")
    print("Therefore the numbers are not equal.")
    print("And the second number is greater than the first number.")
else:
    print(f"{first_number} is equal to {second_number}.")

fav_animal = input("What is your favorite animal? ")
if fav_animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
    