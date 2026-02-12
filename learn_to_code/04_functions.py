"""
===========================================
  LESSON 4: FUNCTIONS
===========================================

A function is a reusable block of code that performs a specific task.
You define it once, then call it whenever you need it.

Think of a function like a recipe: you write it once, then follow it
whenever you want to make that dish.
"""

# ── SECTION 1: Defining and Calling Functions ─────────────

# Use 'def' to define a function
def say_hello():
    print("Hello, World!")

# Call the function by using its name followed by ()
print("── Section 1: Basic Functions ──")
say_hello()
say_hello()  # You can call it as many times as you want
print()


# ── SECTION 2: Parameters and Arguments ───────────────────

# Parameters let you pass data INTO a function
def greet(name):
    print(f"Hello, {name}!")

# The value you pass in is called an "argument"
print("── Section 2: Parameters ──")
greet("Alice")
greet("Bob")
print()

# Multiple parameters
def introduce(name, age, hobby):
    print(f"Hi, I'm {name}. I'm {age} and I like {hobby}.")

introduce("Cristiano", 25, "coding")
print()


# ── SECTION 3: Return Values ─────────────────────────────

# Functions can send a value BACK using 'return'
def add(a, b):
    return a + b

def square(n):
    return n * n

print("── Section 3: Return Values ──")
result = add(5, 3)
print(f"add(5, 3) = {result}")
print(f"square(4) = {square(4)}")

# You can use returned values in expressions
total = add(10, 20) + add(30, 40)
print(f"add(10, 20) + add(30, 40) = {total}")
print()


# ── SECTION 4: Default Parameters ────────────────────────

# You can give parameters default values
def make_coffee(size="medium", sugar=1):
    print(f"Making a {size} coffee with {sugar} sugar(s).")

print("── Section 4: Default Parameters ──")
make_coffee()                    # Uses all defaults
make_coffee("large")             # Override size
make_coffee("small", 3)          # Override both
make_coffee(sugar=0)             # Use keyword argument to skip 'size'
print()


# ── SECTION 5: Scope ─────────────────────────────────────

# Variables created INSIDE a function only exist inside that function.
# This is called "local scope".

print("── Section 5: Scope ──")

message = "I'm global"  # This variable exists everywhere

def show_scope():
    local_var = "I'm local"  # This only exists inside the function
    print(f"  Inside function: {message}")  # Can see global variable
    print(f"  Inside function: {local_var}")

show_scope()
print(f"  Outside function: {message}")
# print(local_var)  # This would cause an ERROR - local_var doesn't exist here
print()


# ── SECTION 6: Functions Calling Functions ────────────────

# Functions can call other functions - this is how you build complex programs

def calculate_area(width, height):
    return width * height

def calculate_price(area, price_per_sqft):
    return area * price_per_sqft

def get_room_quote(width, height, price_per_sqft):
    area = calculate_area(width, height)
    price = calculate_price(area, price_per_sqft)
    return area, price  # You can return multiple values!

print("── Section 6: Functions Calling Functions ──")
area, price = get_room_quote(12, 10, 8.50)
print(f"Room: 12x10 ft")
print(f"Area: {area} sq ft")
print(f"Price: ${price:.2f}")
print()


# ── SECTION 7: Practical Example ──────────────────────────

# Let's build a simple calculator using functions

def calculator(num1, num2, operation):
    """Perform a math operation on two numbers.

    This text in triple quotes is called a 'docstring'.
    It documents what the function does.
    """
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero"
        return num1 / num2
    else:
        return "Error: Unknown operation"

print("── Section 7: Calculator ──")
print(f"10 + 5 = {calculator(10, 5, '+')}")
print(f"10 - 5 = {calculator(10, 5, '-')}")
print(f"10 * 5 = {calculator(10, 5, '*')}")
print(f"10 / 5 = {calculator(10, 5, '/')}")
print(f"10 / 0 = {calculator(10, 0, '/')}")
print()


# ── SECTION 8: Interactive Example ────────────────────────

print("── Section 8: Try It ──")

def is_palindrome(text):
    """Check if a word reads the same forwards and backwards."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

word = input("Enter a word to check if it's a palindrome: ")
if is_palindrome(word):
    print(f"'{word}' IS a palindrome!")
else:
    print(f"'{word}' is NOT a palindrome.")

print()


# ═══════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════

# Exercise 1: Write a function called 'celsius_to_fahrenheit' that
#             takes a Celsius temperature and returns Fahrenheit.
#             Formula: F = C * 9/5 + 32
#
# def celsius_to_fahrenheit(celsius):
#     return ___
#
# print(celsius_to_fahrenheit(0))    # Should print 32.0
# print(celsius_to_fahrenheit(100))  # Should print 212.0

# Exercise 2: Write a function called 'is_even' that returns True
#             if a number is even, False otherwise.
#             Then use it in a loop to print even numbers from 1-20.
#
# def is_even(n):
#     return ___
#
# for i in range(1, 21):
#     if is_even(i):
#         print(i)

# Exercise 3: Write a function called 'count_vowels' that takes a
#             string and returns the number of vowels (a, e, i, o, u).
#
# def count_vowels(text):
#     count = 0
#     for char in text.lower():
#         if char in "aeiou":
#             count += 1
#     return count
#
# print(count_vowels("Hello World"))  # Should print 3
