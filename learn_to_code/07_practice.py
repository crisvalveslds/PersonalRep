"""
===========================================
  PRACTICE: COMBINED EXERCISES
===========================================

These exercises combine concepts from all the lessons.
They're designed to challenge you and reinforce what you've learned.

Try to solve each one on your own before looking at the hints!
"""

print("=" * 50)
print("  CODING PRACTICE CHALLENGES")
print("=" * 50)
print()


# ── CHALLENGE 1: Number Analyzer ─────────────────────────
# Difficulty: Easy

print("── Challenge 1: Number Analyzer ──")
print("Enter numbers one at a time. Type 'done' when finished.")
print()

numbers = []
while True:
    user_input = input("Enter a number (or 'done'): ")
    if user_input.lower() == "done":
        break
    try:
        numbers.append(float(user_input))
    except ValueError:
        print("That's not a valid number. Try again.")

if numbers:
    print(f"\nYou entered {len(numbers)} number(s):")
    print(f"  Numbers: {numbers}")
    print(f"  Sum:     {sum(numbers)}")
    print(f"  Average: {sum(numbers) / len(numbers):.2f}")
    print(f"  Min:     {min(numbers)}")
    print(f"  Max:     {max(numbers)}")
    positive = [n for n in numbers if n > 0]
    negative = [n for n in numbers if n < 0]
    print(f"  Positive: {len(positive)}, Negative: {len(negative)}")
else:
    print("No numbers entered.")

print()


# ── CHALLENGE 2: Word Frequency Counter ──────────────────
# Difficulty: Medium

print("── Challenge 2: Word Frequency Counter ──")
print()

text = input("Enter a sentence: ")

# Count how often each word appears
words = text.lower().split()
frequency = {}

for word in words:
    # Remove punctuation from the word
    cleaned = ""
    for char in word:
        if char.isalpha():
            cleaned += char

    if cleaned:
        if cleaned in frequency:
            frequency[cleaned] += 1
        else:
            frequency[cleaned] = 1

# Sort by frequency (most common first)
sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

print("\nWord frequencies:")
for word, count in sorted_words:
    bar = "#" * count
    print(f"  {word:15} {bar} ({count})")

print()


# ── CHALLENGE 3: Password Strength Checker ───────────────
# Difficulty: Medium

print("── Challenge 3: Password Strength Checker ──")
print()


def check_password(password):
    """Check password strength and return a score with feedback."""
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters")

    if len(password) >= 12:
        score += 1

    # Check for uppercase
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
    else:
        feedback.append("Add uppercase letters")

    # Check for lowercase
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
    else:
        feedback.append("Add lowercase letters")

    # Check for digits
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
    else:
        feedback.append("Add numbers")

    # Check for special characters
    special = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    has_special = False
    for char in password:
        if char in special:
            has_special = True
            break
    if has_special:
        score += 1
    else:
        feedback.append("Add special characters (!@#$...)")

    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, feedback


password = input("Enter a password to check: ")
strength, score, feedback = check_password(password)

print(f"\n  Strength: {strength} ({score}/6)")
meter = "[" + "#" * score + "-" * (6 - score) + "]"
print(f"  Meter:    {meter}")

if feedback:
    print("  Tips to improve:")
    for tip in feedback:
        print(f"    - {tip}")

print()


# ── CHALLENGE 4: Simple Inventory System ─────────────────
# Difficulty: Harder

print("── Challenge 4: Mini Inventory System ──")
print()

inventory = {
    "apple": {"price": 0.50, "quantity": 100},
    "banana": {"price": 0.30, "quantity": 150},
    "orange": {"price": 0.75, "quantity": 80},
    "milk": {"price": 2.99, "quantity": 50},
    "bread": {"price": 1.50, "quantity": 30},
}


def show_inventory(inv):
    print(f"  {'Item':<12} {'Price':>8} {'Qty':>6} {'Value':>10}")
    print(f"  {'-'*12} {'-'*8} {'-'*6} {'-'*10}")
    total_value = 0
    for item, info in inv.items():
        value = info['price'] * info['quantity']
        total_value += value
        print(f"  {item:<12} ${info['price']:>7.2f} {info['quantity']:>6} ${value:>9.2f}")
    print(f"  {'':12} {'':8} {'':6} {'-'*10}")
    print(f"  {'Total Value':<28} ${total_value:>9.2f}")


def process_sale(inv, item, qty):
    if item not in inv:
        print(f"  '{item}' not found in inventory.")
        return 0
    if inv[item]["quantity"] < qty:
        print(f"  Not enough {item} in stock (have {inv[item]['quantity']}).")
        return 0
    inv[item]["quantity"] -= qty
    total = inv[item]["price"] * qty
    print(f"  Sold {qty} {item}(s) for ${total:.2f}")
    return total


print("Current Inventory:")
show_inventory(inventory)
print()

# Interactive sale
item = input("What would you like to buy? ").lower().strip()
if item in inventory:
    qty = int(input(f"How many {item}(s)? "))
    process_sale(inventory, item, qty)
    print("\nUpdated Inventory:")
    show_inventory(inventory)
else:
    print(f"Sorry, we don't have '{item}'.")

print()
print("=" * 50)
print("  Great job completing the practice challenges!")
print("  Keep coding and building projects!")
print("=" * 50)
