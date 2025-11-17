# Adventure Game
import sys

car_was_destroyed = False
injured_by_wolf = False
leg_was_treated = False
fuse_found = False

print("Welcome to the Adventure Game!")
print("It's dark and windy when your car suddenly broke down.")
print("The engine tries to start, but it won't budge.")
print("As you think about what to do, you notice that the hour is late.")
print("----------------------------------")

# First circle of decisions
decision_1 = input("Should you try again to start the car or seek help? (Type 'TRY' or 'HELP') ")
if decision_1.lower() == 'try':
    print("As you try to start the car again, you hear a strange noise.")
    decision_2 = input("Do you keep trying to start the car or get out and seek help? (Type 'TRY' or 'HELP') ")
    if decision_2.lower() == 'try':
        print("With each new attempt, the noise gets louder and more unsettling.")
        print("Something tells you that you should stop, but you are determined to get the car started.")
        decision_3 = input("Will you try one last time or look for help? (Type 'TRY' or 'HELP') ")
        if decision_3.lower() == 'try':
            print("As you try one more time, the car suddenly bursts into flames!")
            print("You quickly exit the vehicle and run to safety, but you are now stranded in the dark.")
            print("The only hope that you had of leaving the area is now gone.")
            car_was_destroyed = True
            print("As you look around, you see a house on a hill with a faint light in the distance.")
        elif decision_3.lower() == 'help':
            print("As you exit the car, you notice some smoke coming from the engine.")
            print("But it soon dissipates, and you feel relieved that you didn't break the engine.")
            print("As you check the reason the car wouldn't start, you notice that one of the fuses has blown, you need to find a new one quickly.")
            print("Just ahead you find a path that leads to a house on a hill, with smoke coming out of the chimney.")
        else:
            print("Invalid choice. Please restart the game and choose a valid option.")
            sys.exit()
    elif decision_2.lower() == 'help':
        print("You notice a light indicating that one of the fuses has blown, you need to find a new one quickly, if you want to get the car started.")
        print("You leave the car behind and seek help.")
        print("Just around you see a path that leads to a house on a hill not far from you.")
    else:
        print("Invalid choice. Please restart the game and choose a valid option.")
        sys.exit()
elif decision_1.lower() == 'help':
    print("The panel shows that one of the fuses has died, you need to find a new one to get the car running again.")
    print("On the distance you see a house on a hill and decide to seek help.")
else:
    print("Invalid choice. Please restart the game and choose a valid option.")
    sys.exit()

print("----------------------------------")

# The game can continue from here with further decisions and outcomes.