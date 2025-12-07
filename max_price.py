shopping_cart = [
    ["Chips", 2.99],
    ["Bread", 2.50],
    ["Milk", 3.19],
    ["Ice Cream", 6.99],
    ["Cheese", 5.99],
    ["Candy bar", 0.99]
]

max_price = 0
item_max = ""

for item in shopping_cart:
    if item[1] > max_price:
        max_price = item[1]
        item_max = item

print(f"The most expensive item is: {item_max[0]} - ${item_max[1]:.2f}")


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

age = 200
person = ""

for friend in people:
    if int(friend.split()[1]) < age:
        age = int(friend.split()[1])
        person = friend.split()

print(f"The youngest person is: {person[0]}")