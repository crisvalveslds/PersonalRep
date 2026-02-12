"""
===========================================
  LESSON 6: FILE INPUT / OUTPUT
===========================================

Programs can read data from files and write data to files.
This is essential for working with real-world data.
"""

import os

# Get the directory this script is in, so file paths work correctly
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# ── SECTION 1: Writing to a File ─────────────────────────

print("── Section 1: Writing Files ──")

# 'w' mode = write (creates file or overwrites existing content)
file_path = os.path.join(SCRIPT_DIR, "example_output.txt")
with open(file_path, "w") as file:
    file.write("Hello, File!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

print(f"Wrote 3 lines to example_output.txt")

# 'a' mode = append (adds to the end without erasing)
with open(file_path, "a") as file:
    file.write("This line was appended.\n")

print("Appended 1 more line.")
print()

# NOTE: The 'with' statement automatically closes the file when done.
# This is the recommended way to work with files in Python.


# ── SECTION 2: Reading from a File ───────────────────────

print("── Section 2: Reading Files ──")

# Read the entire file at once
with open(file_path, "r") as file:
    content = file.read()
    print("Full content:")
    print(content)

# Read line by line (better for large files)
print("Line by line:")
with open(file_path, "r") as file:
    for line_number, line in enumerate(file, 1):
        # .strip() removes the newline character at the end
        print(f"  Line {line_number}: {line.strip()}")

print()

# Read all lines into a list
with open(file_path, "r") as file:
    lines = file.readlines()
    print(f"Number of lines: {len(lines)}")

print()


# ── SECTION 3: Working with CSV Data ─────────────────────

print("── Section 3: CSV Files ──")

# CSV = Comma-Separated Values, a common data format
# Let's create a sample CSV file first

csv_path = os.path.join(SCRIPT_DIR, "students.csv")
with open(csv_path, "w") as file:
    file.write("name,age,grade\n")
    file.write("Alice,20,A\n")
    file.write("Bob,22,B\n")
    file.write("Charlie,21,A\n")
    file.write("Diana,23,B\n")

# Now read and process the CSV
students = []

with open(csv_path, "r") as file:
    header = file.readline().strip().split(",")  # Read first line as headers
    print(f"Headers: {header}")

    for line in file:
        values = line.strip().split(",")
        student = {
            "name": values[0],
            "age": int(values[1]),
            "grade": values[2]
        }
        students.append(student)

print("Students:")
for s in students:
    print(f"  {s['name']} (age {s['age']}) - Grade: {s['grade']}")

# Filter: find all A students
a_students = [s["name"] for s in students if s["grade"] == "A"]
print(f"A students: {a_students}")
print()


# ── SECTION 4: Error Handling with Files ──────────────────

print("── Section 4: Error Handling ──")

# What if the file doesn't exist? Use try/except to handle errors.
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found! (This is expected - we handled the error.)")

# Check if a file exists before opening
if os.path.exists(file_path):
    print(f"'{file_path}' exists!")
else:
    print(f"'{file_path}' does not exist.")

print()


# ── SECTION 5: Practical Example ─────────────────────────

print("── Section 5: Simple To-Do List ──")

todo_path = os.path.join(SCRIPT_DIR, "my_todos.txt")


def load_todos():
    """Load to-do items from file."""
    if not os.path.exists(todo_path):
        return []
    with open(todo_path, "r") as file:
        return [line.strip() for line in file if line.strip()]


def save_todos(todos):
    """Save to-do items to file."""
    with open(todo_path, "w") as file:
        for todo in todos:
            file.write(todo + "\n")


def show_todos(todos):
    """Display all to-do items."""
    if not todos:
        print("  (No items yet)")
    else:
        for i, todo in enumerate(todos, 1):
            print(f"  {i}. {todo}")


# Demo the to-do list
todos = load_todos()

# Add some sample items for demonstration
if not todos:
    todos = ["Learn Python basics", "Practice loops", "Build a project"]
    save_todos(todos)

print("Your to-do list:")
show_todos(todos)
print()

action = input("Add an item to your to-do list (or press Enter to skip): ")
if action.strip():
    todos.append(action.strip())
    save_todos(todos)
    print("\nUpdated to-do list:")
    show_todos(todos)

print()


# Clean up example files (comment these out if you want to keep them)
# os.remove(file_path)
# os.remove(csv_path)
# os.remove(todo_path)


# ═══════════════════════════════════════════════════════════
# PRACTICE EXERCISES
# ═══════════════════════════════════════════════════════════

# Exercise 1: Write a program that asks the user for their name and
#   favorite color, then saves it to a file called "favorites.txt".
#   Run the program multiple times - each entry should be appended
#   (not overwritten). Then read and display all entries.

# Exercise 2: Create a program that reads a text file and counts:
#   - The number of lines
#   - The number of words
#   - The number of characters
#   (Hint: use split() to count words)

# Exercise 3: Create a simple gradebook:
#   - Write a CSV file with columns: student_name, test1, test2, test3
#   - Read it back and calculate each student's average
#   - Find the student with the highest average
