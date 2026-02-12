"""
===========================================
  LESSON 3: LOOPS (for and while)
===========================================

Loops let you repeat code multiple times without rewriting it.
Python has two types of loops: 'for' and 'while'.
"""

# ── SECTION 1: The for Loop ──────────────────────────────

# A for loop repeats code for each item in a sequence
print("── Section 1: for Loop Basics ──")

# Loop through a list of items
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

print()

# Loop through a range of numbers
# range(5) gives you 0, 1, 2, 3, 4
print("Counting to 5:")
for i in range(5):
    print(f"  {i}")

print()

# range(start, stop) - from start up to (not including) stop
print("Numbers 1 through 5:")
for i in range(1, 6):
    print(f"  {i}")

print()

# range(start, stop, step) - count by step
print("Even numbers from 2 to 10:")
for i in range(2, 11, 2):
    print(f"  {i}")

print()


# ── SECTION 2: The while Loop ────────────────────────────

# A while loop keeps running as long as its condition is True
print("── Section 2: while Loop ──")

count = 1
while count <= 5:
    print(f"  Count is {count}")
    count += 1  # same as: count = count + 1
    # Without this line, the loop would run FOREVER! (infinite loop)

print()


# ── SECTION 3: Building Things with Loops ─────────────────

# Loops are great for accumulating results
print("── Section 3: Accumulating Values ──")

# Sum all numbers from 1 to 100
total = 0
for number in range(1, 101):
    total += number

print(f"Sum of 1 to 100 = {total}")

# Build a string character by character
word = "Python"
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

print(f"'{word}' reversed is '{reversed_word}'")
print()


# ── SECTION 4: break and continue ─────────────────────────

# break - exits the loop immediately
# continue - skips the rest of THIS iteration and goes to the next one

print("── Section 4: break and continue ──")

# break example: stop searching when we find what we need
print("Searching for 'cherry':")
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(f"  Checking {fruit}...")
    if fruit == "cherry":
        print(f"  Found it: {fruit}!")
        break  # Stop the loop, we found it

print()

# continue example: skip certain items
print("Odd numbers only (skip evens):")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"  {i}")

print()


# ── SECTION 5: Nested Loops ──────────────────────────────

# A loop inside another loop
print("── Section 5: Nested Loops ──")
print("Multiplication table (1-5):")
print()

# Print header
print("    ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print()
print("   " + "----" * 5)

# Print table
for row in range(1, 6):
    print(f"{row:2} |", end="")
    for col in range(1, 6):
        print(f"{row * col:4}", end="")
    print()  # New line after each row

print()


# ── SECTION 6: Looping with enumerate and zip ────────────

print("── Section 6: enumerate and zip ──")

# enumerate gives you both the index AND the value
colors = ["red", "green", "blue"]
print("Colors with index:")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

print()

# zip combines two lists together, pairing items by position
names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
print("Names with scores:")
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

print()


# ── SECTION 7: Interactive Example ────────────────────────

print("── Section 7: Guessing Game ──")
import random

secret = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20.")

while True:  # Loop forever until we break
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print(f"Correct! You got it in {attempts} attempt(s)!")
        break  # Exit the loop

print()


# ═══════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════

# Exercise 1: Print all numbers from 1 to 50 that are divisible by 7.
#
# for i in range(___):
#     if ___:
#         print(i)

# Exercise 2: Ask the user for a word. Print each letter on its own line
#             along with its position (starting from 1).
#             Example: "Hi" -> "1: H" then "2: i"
#
# word = input("Enter a word: ")
# for ___, ___ in enumerate(___):
#     print(f"{___}: {___}")

# Exercise 3: Write a program that keeps asking the user for numbers
#             until they type "done". Then print the total and average.
#
# total = 0
# count = 0
# while True:
#     user_input = input("Enter a number (or 'done'): ")
#     if user_input == "done":
#         break
#     total += float(user_input)
#     count += 1
# if count > 0:
#     print(f"Total: {total}, Average: {total / count}")
