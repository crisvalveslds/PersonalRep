# I added a second adjective and an extra verb and a snack to make the story more interesting.
# Now, by the end the animal becomes the new best friend of the narrator!

print('Please enter the following:')
print()
adjective1 = input('adjective: ')
animal = input('animal: ')
verb1 = input('verb: ')
exclamation = input('exclamation: ')
verb2 = input('verb: ')
verb3 = input('verb: ')
verb4 = input('verb: ')
snack = input('snack: ')
adjective2 = input('adjective: ')

print()
print('Your story is:')
print()
print(
        f'The other day, I was really in trouble. It all started when I saw a very {adjective1.lower()} {animal.lower()} {verb1.lower()} down the hallway. '
        f'"{exclamation.capitalize()}!" I yelled. But all I could think to do was to {verb2.lower()} over and over. '
        f'Miraculously, that caused it to stop, but not before it tried to {verb3.lower()} right in front of my family.'
      )
print(
        f'Later, when things calmed down, we discovered that the {animal.lower()} was just hungry. '
        f'After I gave it some {snack.lower()}, it started to {verb4.lower()} happily all over the floor. '
        f'Who knew that a {adjective2.lower()} {animal.lower()} could become my new best friend?'
    )