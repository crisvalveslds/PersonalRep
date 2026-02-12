"""
===========================================
  LESSON 1: VARIABLES AND DATA TYPES
===========================================

A variable is like a labeled box that holds a value.
You create one by choosing a name and using = to assign a value.
"""

# ── SECTION 1: Creating Variables ──────────────────────────

# Strings: text wrapped in quotes
name = "Cristiano"
greeting = 'Hello, World!'

# Integers: whole numbers (no decimals)
age = 25
year = 2026

# Floats: numbers with decimals
price = 9.99
temperature = 36.6

# Booleans: True or False
is_student = True
is_raining = False

print("── Section 1: Variables ──")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price: {price}")
print(f"Is student: {is_student}")
print()


# ── SECTION 2: Data Types ─────────────────────────────────

# You can check what type a variable is using type()
print("── Section 2: Data Types ──")
print(f"type(name)        = {type(name)}")         # <class 'str'>
print(f"type(age)         = {type(age)}")          # <class 'int'>
print(f"type(price)       = {type(price)}")        # <class 'float'>
print(f"type(is_student)  = {type(is_student)}")   # <class 'bool'>
print()


# ── SECTION 3: Basic Operations ───────────────────────────

# Math with numbers
a = 10
b = 3

print("── Section 3: Math Operations ──")
print(f"{a} + {b} = {a + b}")      # Addition
print(f"{a} - {b} = {a - b}")      # Subtraction
print(f"{a} * {b} = {a * b}")      # Multiplication
print(f"{a} / {b} = {a / b}")      # Division (returns float)
print(f"{a} // {b} = {a // b}")    # Floor division (rounds down)
print(f"{a} % {b} = {a % b}")      # Modulus (remainder)
print(f"{a} ** {b} = {a ** b}")    # Exponent (10 to the power of 3)
print()


# ── SECTION 4: String Operations ──────────────────────────

first_name = "Cristiano"
last_name = "Alves"

# Concatenation: joining strings together
full_name = first_name + " " + last_name

# f-strings: embedding variables inside strings (the modern way)
message = f"Hello, my name is {full_name}."

# String methods
print("── Section 4: String Operations ──")
print(f"Full name: {full_name}")
print(f"Uppercase: {full_name.upper()}")
print(f"Lowercase: {full_name.lower()}")
print(f"Length: {len(full_name)} characters")
print(f"First letter: {full_name[0]}")
print(f"Last letter: {full_name[-1]}")
print()


# ── SECTION 5: Getting User Input ─────────────────────────

# input() pauses the program and waits for the user to type something.
# It ALWAYS returns a string, even if they type a number.

print("── Section 5: User Input ──")
user_name = input("What is your name? ")
print(f"Nice to meet you, {user_name}!")

# To get a number from the user, convert the string:
user_age = input("How old are you? ")
user_age = int(user_age)  # Convert string to integer
next_year = user_age + 1
print(f"Next year you'll be {next_year}!")
print()


# ── SECTION 6: Type Conversion ────────────────────────────

# Converting between types
number_as_string = "42"
number_as_int = int(number_as_string)       # String -> Integer
number_as_float = float(number_as_string)   # String -> Float
back_to_string = str(number_as_int)         # Integer -> String

print("── Section 6: Type Conversion ──")
print(f"String '42' -> int: {number_as_int} (type: {type(number_as_int).__name__})")
print(f"String '42' -> float: {number_as_float} (type: {type(number_as_float).__name__})")
print(f"Int 42 -> string: '{back_to_string}' (type: {type(back_to_string).__name__})")
print()


# ═══════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# Try these on your own! Uncomment and fill in the blanks.
# ═══════════════════════════════════════════════════════════

# Exercise 1: Create variables for your favorite movie, its release year,
#             and its rating (out of 10). Print them all in one sentence.
#
# movie = ___
# release_year = ___
# rating = ___
# print(f"My favorite movie is {movie} ({release_year}), rated {rating}/10")

# Exercise 2: Ask the user for two numbers, add them together,
#             and print the result.
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"{num1} + {num2} = {___}")

# Exercise 3: Calculate the area of a rectangle.
#             Area = width * height
#
# width = float(input("Enter width: "))
# height = float(input("Enter height: "))
# area = ___
# print(f"The area is {area}")
