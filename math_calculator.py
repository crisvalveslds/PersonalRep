numbers = []

print("Enter a list of numbers, type 0 when you are finished.")

while True:
    number = int(input("Enter a number: "))
    if number == 0:
        break
    else:
        numbers.append(number)

sum = 0
for item in numbers:
    sum += item

average = sum / len(numbers)

largest = 0
smallest = max(numbers)

for item in numbers:
    if item > largest:
        largest = item
    if (item < smallest) and (item > 0):
        smallest = item

print(f"The sum is: {sum}")
print(f"The average is: {average:.2f}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest}")
