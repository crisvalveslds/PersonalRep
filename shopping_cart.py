# Shopping Cart Program
# It was interesting learning about lists, how to append and pop out items
# As well as how to iterate on its items
# I added the option to ship the products in the shopping cart
# It uses a previously saved address and a previous payment method to process and ship it
# And then it cleans the shopping cart to start over.

products = []
prices = []

print("Welcome to the Shopping Cart Program!\n")

while True:
    print("Please select one of the options:")
    print("1. View cart")
    print("2. Add item")
    print("3. Remove item")
    print("4. Total")
    print("5. Ship Items")
    print("6. Quit")
    option = int(input("Please enter an option: "))
    
    if option == 1:
        if len(products) == 0:
            print("Your cart is empty.\n")
        else:
            print("\nHere is your cart: ")
            for i in range(len(products)):
                print(f"{i+1}. {products[i]} - ${prices[i]:.2f}")
            print("")
    elif option == 2:
        print("\nLet's add some items to your cart!")
        while True:
            product = input("Enter an item: ")
            price = float(input(f"Enter the price for {product}: "))
            products.append(product)
            prices.append(price)
            print(f"{product} has been added to your cart.")
            answer = input("Add another product (y/n)? ")
            if answer == "n":
                print("")
                break
    elif option == 3:
        if len(products) == 0:
            print("\nYour cart is empty. There are no items to remove.")
        else:
            print("\nHere is your cart: ")
            for i in range(len(products)):
                print(f"{i+1}. {products[i]} - ${prices[i]:.2f}")
            remove = int(input("Which item would you like to remove? "))
            while (remove < 0) or (remove > len(products)):
                print("Item is not in your cart.")
                remove = int(input("Which item would you like to remove? "))
            item_to_remove = products[remove-1]
            products.pop(remove-1)
            prices.pop(remove-1)
            print(f"{item_to_remove} has been removed from your cart.\n")
    elif option == 4:
        total = 0
        for price in prices:
            total += price
        print(f"The total for your shopping cart is: ${total:.2f}\n")
    elif option == 5:
        total = 0
        print("\nThe following items were shipped to your address!")
        for i in range(len(products)):
            print(f"{i+1}. {products[i]} - ${prices[i]:.2f}")
            total += prices[i]
        print(f"The total debited from your card is: ${total:.2f}\n")
        print("Thank you for shopping with us!")
        products.clear()
        prices.clear()
        print("Your cart is now empty!")
    elif option == 6:
        print("Thank you for shopping with us!")
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")