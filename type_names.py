friends = []

while True:
    test = input("Enter a friend's name: ")
    if test == "end":
        break
    if test in friends:
        print("This friend is already in your list.")
    else:
        friends.append(test)

if len(friends) == 0:
    print("You have no friends.")
else:
    print("Your friends are: ")
    for friend in friends:
        print(friend)
