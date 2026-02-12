"""
===========================================
  LESSON 5: LISTS AND DICTIONARIES
===========================================

Collections let you store multiple values in a single variable.
Lists are ordered sequences. Dictionaries store key-value pairs.
"""

# ── SECTION 1: Lists ─────────────────────────────────────

print("── Section 1: Lists ──")

# A list is an ordered collection of items
colors = ["red", "green", "blue"]
numbers = [10, 20, 30, 40, 50]
mixed = ["hello", 42, True, 3.14]  # Lists can hold different types

print(f"Colors: {colors}")
print(f"Numbers: {numbers}")
print()

# Accessing items by index (starts at 0!)
#         Index:   0       1       2
#                 "red"  "green"  "blue"
print(f"First color: {colors[0]}")   # red
print(f"Last color: {colors[-1]}")   # blue (negative = from the end)
print(f"Middle: {colors[1]}")        # green
print()


# ── SECTION 2: Modifying Lists ───────────────────────────

print("── Section 2: Modifying Lists ──")

fruits = ["apple", "banana", "cherry"]
print(f"Original: {fruits}")

# Add items
fruits.append("date")           # Add to the end
print(f"After append: {fruits}")

fruits.insert(1, "avocado")     # Insert at a specific position
print(f"After insert: {fruits}")

# Remove items
fruits.remove("banana")         # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()           # Remove and return the last item
print(f"Popped: {popped}")
print(f"After pop: {fruits}")

# Sort
numbers = [64, 25, 12, 22, 11]
numbers.sort()
print(f"Sorted: {numbers}")

print(f"Length: {len(numbers)}")
print()


# ── SECTION 3: List Slicing ──────────────────────────────

print("── Section 3: Slicing ──")

letters = ["a", "b", "c", "d", "e", "f"]
#           0     1     2     3     4     5

# slice = list[start:stop]  (start is included, stop is NOT)
print(f"All: {letters}")
print(f"[1:4]: {letters[1:4]}")    # ['b', 'c', 'd']
print(f"[:3]:  {letters[:3]}")     # ['a', 'b', 'c']  (from beginning)
print(f"[3:]:  {letters[3:]}")     # ['d', 'e', 'f']  (to end)
print(f"[::2]: {letters[::2]}")    # ['a', 'c', 'e']  (every 2nd item)
print()


# ── SECTION 4: Useful List Operations ────────────────────

print("── Section 4: List Operations ──")

numbers = [3, 7, 1, 9, 4, 6, 2, 8, 5]

print(f"Numbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.1f}")
print(f"5 in list? {5 in numbers}")    # Check membership
print(f"99 in list? {99 in numbers}")
print()


# ── SECTION 5: Dictionaries ──────────────────────────────

print("── Section 5: Dictionaries ──")

# A dictionary stores key-value pairs
# Think of it like a real dictionary: word -> definition

student = {
    "name": "Cristiano",
    "age": 25,
    "courses": ["CSE 110", "CSE 111"],
    "gpa": 3.8
}

# Access values by key
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Courses: {student['courses']}")
print()

# Add or update entries
student["email"] = "cristiano@example.com"  # Add new key
student["age"] = 26                          # Update existing key
print(f"Updated: {student}")
print()


# ── SECTION 6: Looping Through Dictionaries ──────────────

print("── Section 6: Looping Through Dictionaries ──")

scores = {
    "Alice": 95,
    "Bob": 87,
    "Charlie": 92,
    "Diana": 88
}

# Loop through keys
print("Students:")
for name in scores:
    print(f"  {name}")

print()

# Loop through keys AND values
print("Scores:")
for name, score in scores.items():
    print(f"  {name}: {score}")

print()

# Check if a key exists
if "Alice" in scores:
    print(f"Alice's score: {scores['Alice']}")

print()


# ── SECTION 7: List Comprehensions ───────────────────────

# A concise way to create lists from existing data
print("── Section 7: List Comprehensions ──")

# The long way:
squares_long = []
for i in range(1, 6):
    squares_long.append(i ** 2)

# The short way (list comprehension):
squares = [i ** 2 for i in range(1, 6)]

print(f"Squares: {squares}")

# With a condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print(f"Even squares: {even_squares}")

# Transform a list
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(f"Capitalized: {capitalized}")
print()


# ── SECTION 8: Practical Example ─────────────────────────

print("── Section 8: Contact Book ──")

contacts = {}

# Add some contacts
sample_contacts = [
    ("Alice", "555-0101"),
    ("Bob", "555-0102"),
    ("Charlie", "555-0103"),
]

for name, phone in sample_contacts:
    contacts[name] = phone

# Look up a contact
print("Your contacts:")
for name, phone in contacts.items():
    print(f"  {name}: {phone}")

print()
search = input("Search for a contact (name): ")
if search in contacts:
    print(f"  {search}'s number: {contacts[search]}")
else:
    print(f"  '{search}' not found in contacts.")

print()


# ═══════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════

# Exercise 1: Create a list of 5 of your favorite foods.
#   - Print the list
#   - Add a 6th food
#   - Remove the 2nd food
#   - Print the updated list sorted alphabetically

# Exercise 2: Create a dictionary representing a book with keys:
#   title, author, year, pages, genre
#   Print each piece of info in a nice format.

# Exercise 3: Given the list below, use a list comprehension to create
#   a new list containing only the words that are longer than 4 characters.
#
# words = ["hi", "hello", "hey", "greetings", "yo", "good morning"]
# long_words = [___ for ___ in words if ___]
# print(long_words)  # Should print: ['hello', 'greetings', 'good morning']
