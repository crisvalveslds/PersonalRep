"""
===========================================
  LESSON 2: CONDITIONALS (if / elif / else)
===========================================

Conditionals let your program make decisions.
The code inside an if block only runs when the condition is True.
"""

# ── SECTION 1: Basic if Statement ─────────────────────────

# An if statement checks whether something is True
temperature = 35

print("── Section 1: Basic if ──")
if temperature > 30:
    print(f"{temperature}°C - It's hot outside!")
    # Everything indented under 'if' runs when the condition is True

print()


# ── SECTION 2: if / else ──────────────────────────────────

# else runs when the if condition is False
age = 16

print("── Section 2: if/else ──")
if age >= 18:
    print("You can vote!")
else:
    print("You're not old enough to vote yet.")
    print(f"Wait {18 - age} more year(s).")

print()


# ── SECTION 3: if / elif / else ───────────────────────────

# elif (else if) lets you check multiple conditions in order
score = 85

print("── Section 3: if/elif/else ──")
print(f"Score: {score}")

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
# Python checks each condition top to bottom and stops at the FIRST
# one that's True. Here 85 >= 80 is True, so grade = "B".
print()


# ── SECTION 4: Comparison Operators ───────────────────────

# These are the operators you use in conditions:
#   ==    equal to             (5 == 5 is True)
#   !=    not equal to         (5 != 3 is True)
#   >     greater than         (5 > 3  is True)
#   <     less than            (3 < 5  is True)
#   >=    greater or equal     (5 >= 5 is True)
#   <=    less or equal        (3 <= 5 is True)

x = 10
print("── Section 4: Comparison Operators ──")
print(f"x = {x}")
print(f"x == 10: {x == 10}")
print(f"x != 5:  {x != 5}")
print(f"x > 5:   {x > 5}")
print(f"x < 20:  {x < 20}")
print()


# ── SECTION 5: Logical Operators (and, or, not) ──────────

# Combine multiple conditions
age = 25
has_license = True

print("── Section 5: Logical Operators ──")

# 'and' - BOTH conditions must be True
if age >= 16 and has_license:
    print("You can drive!")

# 'or' - at least ONE condition must be True
is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("No work today!")

# 'not' - flips True to False and vice versa
is_raining = False
if not is_raining:
    print("No umbrella needed.")

print()


# ── SECTION 6: Nested Conditionals ───────────────────────

# You can put if statements inside other if statements
print("── Section 6: Nested Conditionals ──")

has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Welcome to the movie!")
    elif age >= 13:
        print("Welcome! (PG-13 access)")
    else:
        print("Sorry, you need a parent with you.")
else:
    print("You need to buy a ticket first.")

print()


# ── SECTION 7: Interactive Example ────────────────────────

print("── Section 7: Try It Yourself ──")
print("Let's check if a number is positive, negative, or zero.")

user_input = input("Enter a number: ")
number = float(user_input)

if number > 0:
    print(f"{number} is positive!")
elif number < 0:
    print(f"{number} is negative!")
else:
    print("You entered zero!")

print()


# ═══════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════

# Exercise 1: Write a program that asks for a temperature and prints:
#   "Freezing" if below 0
#   "Cold" if 0-15
#   "Warm" if 16-30
#   "Hot" if above 30
#
# temp = float(input("Enter temperature: "))
# if ___:
#     print("Freezing")
# elif ___:
#     ...

# Exercise 2: Write a simple login check.
#   Ask for a username and password.
#   If username is "admin" AND password is "1234", print "Access granted"
#   Otherwise print "Access denied"
#
# username = input("Username: ")
# password = input("Password: ")
# if ___ and ___:
#     ...

# Exercise 3: FizzBuzz - a classic coding challenge!
#   Ask for a number.
#   If divisible by both 3 and 5, print "FizzBuzz"
#   If divisible by 3 only, print "Fizz"
#   If divisible by 5 only, print "Buzz"
#   Otherwise, print the number
#   HINT: Use the modulus operator (%) to check divisibility
#         A number is divisible by 3 if number % 3 == 0
