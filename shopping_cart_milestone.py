items = []

print("Welcome to your shopping list!")
print("Let's add some items to it!")

while True:
    buy = input("Enter an item: ")
    if buy == "quit":
        break
    elif buy in items:
        print("That item is already in your cart.")
    else:
        price = float(input(f"Enter the price for {buy}: "))
        items.append((buy, price))
        print(f"{buy} has been added to your cart.")

if len(items) == 0:
    print("You have no items on your list.")
else:
    print("Here is your cart: ")
    for i in range(len(items)):
        print(f"{i+1}. {items[i][0]} - ${items[i][1]:.2f}")