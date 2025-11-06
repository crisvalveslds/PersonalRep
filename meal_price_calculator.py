# Meal Price Calculator
# I added to the file to include tip, a subtotal with the tip included and a thank you message at the end.

child_meal_price = float(input("How much does a child's meal cost? $"))
adult_meal_price = float(input("How much does an adult's meal cost?: $"))
num_children = int(input("How many children will eat? "))
num_adults = int(input("How many adults will eat? "))

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"The subtotal is: ${subtotal:.2f}")

sales_tax_rate = float(input("What is the sales tax rate for your state? "))
sales_tax = subtotal * (sales_tax_rate / 100)
print(f"The sales tax for this order is: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"The subtotal with taxes is: ${total:.2f}")

tip = float(input("How much would you like to tip your server today? $"))
total_with_tip = total + tip
print(f"Your total with tip is: ${total_with_tip:.2f}")

payment = float(input("How much money will you be using to pay? $"))
change = payment - (total + tip)
print(f"Your change is: ${change:.2f}")
print("Thank you for dining with us today!")