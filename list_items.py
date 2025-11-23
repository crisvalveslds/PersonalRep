shopping_list = []

print("Welcome to your shopping list!")
print("Let's add some items to it!")

while True:
    buy = input("Enter an item: ")
    if buy == "quit":
        break
    if buy in shopping_list:
        print("That item is already in your list.")
    else:
        shopping_list.append(buy)

while True:
    if len(shopping_list) == 0:
        print("You have no items on your list.")
        break
    else:
        print("Here is your shopping list: ")
        for i in range(len(shopping_list)):
            print(f"{i}. {shopping_list[i]}")
    change = input("Would you like to change something (y/n)? ")
    if change == "n":
        break
    if change == "y":
        index = int(input("Which index would you like to change? "))
        new_item = input("What would you like to change it to? ")
        shopping_list[index] = new_item