# Meal Price Calculator
# This is for the milestone.

child_meal_price = float(input("How much does a child's meal cost? $"))
adult_meal_price = float(input("How much does an adult's meal cost?: $"))
num_children = int(input("How many children will eat? "))
num_adults = int(input("How many adults will eat? "))

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print(f"The subtotal is: ${subtotal:.2f}")