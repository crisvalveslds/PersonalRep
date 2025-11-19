# Adventure Game -- Cristiano Alves
# I was very happy to create this game as I love this kind of horror stories that are interactive.
# I asked a friend and my daughter to play the game and they really enjoyed the story and the multiple choices you can make.
# I plan to add more small tweaks to this game in the future and expand it a bit more, maybe even convert it into a playable mini-game.
# This game takes through the events of a special full moon night.
# You can play this multiple times for the different outcomes and especially for the 4 different endings.

import sys
import time
import builtins

def typewriter(text, base_speed=0.03):
    text = str(text)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()

        # Slower pauses on punctuation
        if char in ".!?":
            time.sleep(0.30)
        elif char in ",;:":
            time.sleep(0.15)
        elif char in "-":
            time.sleep(0.01)
        else:
            time.sleep(base_speed)

    sys.stdout.write("\n")
    sys.stdout.flush()


def typewriter_print(*args, speed=0.03, **kwargs):
    # Merge all args into one string (just like real print)
    text = " ".join(str(a) for a in args)
    typewriter(text, base_speed=speed)


# Override the builtin print()
builtins.print = typewriter_print

def invalid_choice():
    print("Invalid choice. Please restart the game and choose a valid option.")
    sys.exit()

def play_game():
    # Variables initialized
    car_was_destroyed = False
    amulet_found = False
    injured_by_wolf = False
    leg_was_treated = False
    coal_used = False
    salve_used = False
    first_aid_used = False
    fuse_found = False
    knife_taken = False
    best_ending_achieved = False

    print("----------------------------------")
    print("Welcome to the Adventure Game!")
    print("----------------------------------")
    print("It's a dark and windy night as you drive back home.")
    print("You knew you shouldn't have listened to that stranger's advice to take the shortcut through the woods.")
    print("You have been noticing this strange light flickering on your dashboard for a while now, but you don't know what it means.")
    print("Suddenly, the car sputters and rolls to a stop.")
    print("You try to start the engine, but it won't turn over.")
    print("As you think about what to do, you realize just how dark it is outside and how far you are from any help.")

    # First circle of decisions
    decision_1 = input("Should you try again to start the car or seek help? (Type 'TRY' or 'HELP') ")
    if decision_1.lower() == 'try':
        print("----------------------------------")
        print("As you turn the key, the engine coughs weakly and you hear a faint clicking sound under the hood.")
        print("The dashboard light flickers again, just for a moment.")
        decision_2 = input("Do you keep trying to start the car or get out and seek help? (Type 'TRY' or 'HELP') ")
        if decision_2.lower() == 'try':
            print("----------------------------------")
            print("The engine stutters harder this time.")
            print("Something rattles beneath the hood, like a loose piece of metal tapping against something.")
            print("For a split second, you think you smell something... sharp? But it's gone before you can be sure.")
            print("Something tells you that you should stop, but you are determined to get the car started.")
            decision_3 = input("Will you try one last time or look for help? (Type 'TRY' or 'HELP') ")
            if decision_3.lower() == 'try':
                print("----------------------------------")
                print("As you try one more time, the dashboard light flares brightly, then dies completely.")
                print("A violent sputter erupts from under the hood, followed by a sudden hiss.")
                print("A strong metallic smell fills the air, and before you can react, the entire front of the car bursts into flames!")
                print("You throw the door open and stumble out, barely escaping the heat.")
                print("The only hope that you had of leaving the area is now gone.")
                car_was_destroyed = True
                print("Now stranded in the dark, you look around and spot a house on a hill with a faint light in the distance.")
            elif decision_3.lower() == 'help':
                print("----------------------------------")
                print("As you step out of the car, you notice a thin wisp of smoke seeping from under the hood.")
                print("It fades quickly, and you feel relieved, it doesn't look like you damaged the engine.")
                print("But a faint burned smell lingers in the air.")
                print("You lean inside and realize the smell comes from beneath the dashboard.")
                print("You check the fuse panel and see that one of the fuses has blown, though you don't know what it was for.")
                print("Without a replacement, you won't be able to get the car started again.")
                print("You step away from the vehicle and spot a narrow path leading to a house on a hill, a faint glow coming from one of its windows.")
            else:
                invalid_choice()
        elif decision_2.lower() == 'help':
            print("----------------------------------")
            print("A faint burned smell drifts from beneath the dashboard.")
            print("You check the fuse box and notice that one of the fuses has blown. You will need a new one, if you want the car to move again.")
            print("You step out of the car to look for help.")
            print("Just ahead, you notice a path leading toward a house on a hill.")
        else:
            invalid_choice()
    elif decision_1.lower() == 'help':
        print("----------------------------------")
        print("You reach for the glove box and open the owner's manual, trying to identify the flickering dashboard light.")
        print("The manual suggests that a fuse may have failed, which would explain the engine trouble.")
        print("You open the fuse panel and find that one of the fuses is indeed blown.")
        print("It's the fuel pump fuse, exactly why the engine refused to start.")
        print("If you had kept trying to turn the key, it might have caused more damage... possibly even a fire.")
        print("In the distance, you notice a house on a hill and decide to head there for help.")
    else:
        invalid_choice()

    print("----------------------------------")

    # Second circle of decisions
    print("As you walk up the hill, the wind howls around you.")
    print("You hear an eerie creaking sound to your left, near the trees.")
    decision_4 = input("Do you want to investigate the sound or continue to the house? (Type 'INVESTIGATE' or 'HOUSE') ")
    if decision_4.lower() == 'investigate':
        print("----------------------------------")
        print("You walk toward the trees and hear a muffled movement shifting in the shadows.")
        print("You can't shake the feeling that something is watching you from the deep darkness.")
        decision_5 = input("Do you want to keep investigating or head back to the house? (Type 'INVESTIGATE' or 'HOUSE') ")
        if decision_5.lower() == 'investigate':
            print("----------------------------------")
            print("As you step closer, an owl suddenly swoops past your head, startling you.")
            print("Something slips deeper into the woods, but the path ahead grows darker and far more unsettling.")
            print("A cold breeze crawls up your spine. You realize you might be in danger.")
            decision_6 = input("Do you want to continue investigating or return to the house? (Type 'INVESTIGATE' or 'HOUSE') ")
            if decision_6.lower() == 'investigate':
                print("----------------------------------")
                print("A pair of glowing eyes appears between the trees, staring directly at you.")
                print("Your heart pounds as you realize this is no ordinary animal. Its low growl sends shivers down your spine.")
                print("As you slowly back away, your eyes locked with the beast's, you step in something.")
                print("You glance down and see a long, curved tooth scratched with faint markings.")
                print("It is wrapped in a thin strip of leather, fallen between the leaves.")
                decision_7 = input("Do you pick it up or leave it? (Type 'PICK' or 'LEAVE') ")
                if decision_7.lower() == 'pick':
                    print("----------------------------------")
                    print("You quickly pocket the tooth, without losing sight of the creature in the shadows.")
                    amulet_found = True
                    print("You have no time to think about what it could be now.")
                    print("You slowly start to back away, hoping that the dark figure won't follow you.")
                    print("The beast's growl intensifies, and it starts to move slowly towards you.")
                elif decision_7.lower() == 'leave':
                    print("----------------------------------")
                    print("You decide to leave the tooth behind and focus on escaping.")
                    print("Whatever it was, surviving is your only priority now.")
                    print("As you step back without taking your eyes off the creature, it moves menacingly in the shadows.")
                else:
                    invalid_choice()
                print("Suddenly, it lunges at you, and you run for dear life!")
                print("You sprint with every ounce of strength and dive inside the house.")
                print("But your speed is not enough. Its jaws clamp around your left leg as you fight to shut the door.")
                print("You kick the animal, finally slamming the door behind you.")
                print("The animal hurls itself at the door, but somehow it holds. Eventually it seems to give up.")
                print("As you stumble forward, a sharp pain explodes in your leg and you feel dizzy.")
                print("You look down and see blood running down your leg. Only then do you realize how deep the wound is.")
                injured_by_wolf = True
                if car_was_destroyed:
                    print("You use your shirt as a makeshift tourniquet, trying desperately to stem the bleeding.")
                    print("Your situation is now dire without the car.")
                    print("You need to find help quickly if you want to survive.")
                else:
                    print("You rip off your shirt and tie it around your leg, trying to stop the bleeding.")
                    print("If you can get the car running again, you might still make it to a hospital.")
                    print("But first, you need to treat the wound before you lose too much blood.")
                    print("Maybe there's something in the house that can help.")
            elif decision_6.lower() == 'house':
                print("----------------------------------")
                print("Your instincts scream for you to run, and you sprint back toward the house.")
                print("You throw yourself inside and slam the door shut behind you.")
                print("You can hear something moving outside, sniffing around the door, but at least you're safe for now.")
            else:
                invalid_choice()
        elif decision_5.lower() == 'house':
            print("----------------------------------")
            print("You decide it's too risky and head straight for the house.")
            print("You can almost feel eyes on your back as you climb the hill, but you refuse to look back.")
            print("You reach the house and rush inside, slamming the door behind you.")
            print("You are safe, but you can't shake the feeling that something is out there.")
        else:
            invalid_choice()
    elif decision_4.lower() == 'house':
        print("----------------------------------")
        print("You turn away from the woods, but the feeling of being watched lingers.")
        print("Uneasy, you hurry up the hill toward the house.")
        print("When you reach the door, you find it slightly ajar.")
        print("You push it open slowly and step inside, quickly locking it behind you.")
        print("If there was something out there, at least you are safe for now.")
    else:
        invalid_choice()

    print("----------------------------------")
    print("As your eyes adjust to the light inside, you find a cozy living room with a fireplace.")

    # Branching consequences of injured_by_wolf
    if injured_by_wolf:
        print("But as you try to walk, the pain intensifies, and you feel dizzy.")
        print("You should look around for something to treat your injury quickly as you are losing blood.")
        print("As you scan the room, you notice a bookshelf and a TV cabinet on different corners.")
        decision_8 = input("Do you want to search the bookshelf or the TV cabinet? (Type 'BOOKSHELF' or 'TVCABINET') ")
        if decision_8.lower() == 'bookshelf':
            print("----------------------------------")
            print("As you search the bookshelf, you find nothing useful for your injury.")
            print("The only thing you notice is an old dusty book about werewolves and a diary.")
            decision_9 = input("Do you want to read the diary or the book about werewolves? (Type 'DIARY' or 'BOOK') ")
            if decision_9.lower() == 'diary':
                print("----------------------------------")
                if amulet_found:
                    print("This seems to be the diary of the owner of the house.")
                    print("Instead of letters you see only strange markings that, somehow, make sense to you.")
                    print("But you don't have time to read it now. You need to treat your wound desperately.")
                    print("You pocket the diary with the amulet and look around for something to help you.")
                    print("You notice a poker on the fireplace with some hot coals nearby.")
                    print("You know that heat can help to cauterize wounds and stop bleeding.")
                    print("You carefully use it to grab a hot coal and press it against your wound.")
                    print("The intense heat causes you to grit your teeth in intense pain.")
                    print("Suddenly, you lose consciousness and collapse to the floor.")
                    print("When you wake up, you feel weak but the bleeding has stopped.")
                    leg_was_treated = True
                    coal_used = True
                    print("As you regain your strength, you hear a strange noise coming from the kitchen.")
                else:
                    print("As you try to read the diary, you feel a sharp pain in your leg.")
                    print("The words on the page seem like gibberish and start to blur as your vision fades.")
                    print("You drop the diary and collapse to the floor.")
                    print("After some time, you wake up feeling weak. It seems you fainted from blood loss.")
                    print("When you finally come to your senses, you hear some noise coming from the kitchen.")
            elif decision_9.lower() == 'book':
                print("----------------------------------")
                print("You open the book and find a recipe for a healing salve.")
                print("The ingredients are neatly tied inside the book, as if someone knew you would need them.")
                print("You prepare and apply the salve to your wound, and although it doesn't completely heal it, it eases the pain significantly.")
                print("You notice that the bleeding has stopped, and you feel a bit more stable now.")
                leg_was_treated = True
                salve_used = True
                print("As you feel better, you hear a noise coming from the kitchen.")
            else:
                invalid_choice()
        elif decision_8.lower() == 'tvcabinet':
            print("----------------------------------")
            print("You search the TV cabinet and find only old magazines and a remote control.")
            print("You hear a faint sound coming from the kitchen, it could be the wind, or maybe it's just your imagination.")
            decision_10 = input("Do you want to keep searching the cabinet or investigate the kitchen? (Type 'SEARCH' or 'KITCHEN') ")
            if decision_10.lower() == 'search':
                print("----------------------------------")
                print("As you open a second drawer, you find an old first aid kit hidden under the magazines!")
                print("You quickly use it to clean and bandage your wound.")
                print("The bandage and salves helps to stop the bleeding, but the pain is still there.")
                leg_was_treated = True
                first_aid_used = True
                print("You realize that you need to get to a hospital if you want to heal completely.")
                print("As you rest for a moment, you hear a noise coming from the kitchen.")
            elif decision_10.lower() == 'kitchen':
                print("----------------------------------")
                print("The pain suddenly intensifies and your vision blurs.")
                print("You collapse on the sofa for a moment, trying to steady yourself.")
                print("After a while, you regain your composure, but you know you need medical help soon.")
                print("When your consciousness returns, you notice a noise coming from the kitchen.")
            else:
                invalid_choice()
        else:
            invalid_choice()
    else:
        print("As you look around, you hear a noise coming from the kitchen.")

    # Branch consequences of car_was_destroyed
    if not car_was_destroyed:
        print("You notice a small desk with a lamp and some papers on it, its drawer is slightly open with several cables hanging out of it.")
        print("The noises from the kitchen suddenly get louder as you move towards it.")
        decision_11 = input("Do you want to search the desk or investigate the noises from the kitchen? (Type 'SEARCH' or 'KITCHEN') ")
        if decision_11.lower() == 'search':
            print("----------------------------------")
            print("You walk over to the desk and open the drawer fully.")
            print("There's a jumble of old papers, with a lot of cables covering everything inside.")
            print("Suddenly, you hear a loud crash from the kitchen, making you flinch.")
            decision_12 = input("Do you want to keep searching the desk or go to the kitchen? (Type 'SEARCH' or 'KITCHEN') ")
            if decision_12.lower() == 'search':
                print("----------------------------------")
                print("You decide to keep searching the desk despite the noise.")
                print("You delve through the mess of cables and papers, determined to find something useful.")
                print("But the sound from the kitchen seems to be approaching, making it hard to concentrate.")
                print("You hear a low growl coming from there, sending chills down your spine.")
                decision_13 = input("Do you want to keep searching the desk or finally go to the kitchen? (Type 'SEARCH' or 'KITCHEN') ")
                if decision_13.lower() == 'search':
                    print("----------------------------------")
                    print("As you sift through the mess, you find a car fuse tucked away at the bottom of the drawer!")
                    print("Feeling relieved, you now have what you need to fix your car.")
                    fuse_found = True
                    print("As you put the fuse in your pocket, the growling from the kitchen grows louder.")
                    print("You realize you need to confront whatever is in there soon.")
                elif decision_13.lower() == 'kitchen':
                    print("----------------------------------")
                    print("You steel yourself and head to the kitchen.")
                    print("As you enter, you see a large wolf rummaging through the cabinets.")
                    print("It seems the door behind the beast was left open, and it must have followed you in.")
                    print("It looks up at you, startled, and growls menacingly.")
                    print("You slowly back away, trying not to provoke it further.")
                    if injured_by_wolf:
                        print("This is the same wolf that bit you earlier.")
                        if not leg_was_treated:
                            print("As it slowly moves toward you, your wound throbs painfully. You can't move.")
                            print("The wolf lunges at you again, but this time, you can't escape its grasp.")
                            print("It bites you in your neck this time, holding you firmly in its grasp. There is no escape.")
                            print("The light fades from your eyes as you succumb to your injuries.")
                            print("GAME OVER")
                            return
                        else: 
                            print("You feel the pain where he bit you earlier. Will you be able to outrun it again?")
                            print("You need to think quickly to avoid another attack.")
                            print("The door behind the kitchen is open, maybe you can make a run for it.")
                    else:
                        print("You realize you need to get out of here quickly.")
                        print("You see the door behind it open, maybe you can outrun it.")
                else:
                    invalid_choice()
            elif decision_12.lower() == 'kitchen':
                print("----------------------------------")
                print("You decide to investigate the kitchen and find out what is making that noise.")
                print("As you approach the door, you see a large wolf sniffing the floor close to the cabinets.")
                print("Someone left the back door open - an easy way for it to slip inside.")
                print("It is sniffing for your scent, growing menacingly.")
                if injured_by_wolf:
                    print("You recognize the wolf that bit you earlier.")
                    if not leg_was_treated:
                        print("Your untreated wound throbs painfully, making it hard to move quickly.")
                        print("While you look for an escape route, the wolf sniffs your scent and turns to face you.")
                        print("It grows menacingly and lunges at you, and this time, you can't escape it.")
                        print("You fight as hard as you can, but you are too weak to resist its strength.")
                        print("You succumb to your injuries shortly after.")
                        print("GAME OVER")
                        return
                    else:
                        print("Your leg was healed, but is still hurting. Will you be able to escape it again?")
                        print("It hasn't noticed you yet, maybe you can make a run for the open door behind the kitchen.")
                else:
                    print("The wolf hasn't completely noticed you yet, but you need to act fast.")
                    print("You see the door behind it open, it might be your only chance to escape.")
            else:
                invalid_choice()
        elif decision_11.lower() == 'kitchen':
            print("----------------------------------")
            print("The noises get your attention and you head to the kitchen.")
            print("From the shadows you see a large wolf sifting through the cabinets.")
            print("Someone left the door behind the kitchen open, and it must have followed you in.")
            print("If you make any sudden movement, it might notice you.")
            if injured_by_wolf:
                print("It's impossible to not recognize the beast that bit you earlier.")
                if not leg_was_treated:
                    print("You try to move, but your wound throbs painfully.")
                    print("As you pull your leg, the pain cuts through you, making you protest loudly.")
                    print("The wolf turns its head towards you, its eyes locking onto yours.")
                    print("Sensing your weakness, it lunges at you again, but this time, you can't escape its grasp.")
                    print("It throws you to the floor and bites you in your neck, there is no mercy.")
                    print("You feel your life slipping away as darkness engulfs you.")
                    print("GAME OVER")
                    return
                else: 
                    print("Your leg is treated, but still painful. Will you have the strength to flee?")
                    print("The door behind the wolf is open, maybe you can run out and get to safety.")
            else:
                print("As it is unaware of your presence, you need to get out quickly.")
                print("The door behind it is open, if you act fast you might escape before it notices you.")
        else:
            invalid_choice()
    else:
        print("----------------------------------")
        print("You need to confront whatever is in there.")
        if not leg_was_treated:
            print("You try to move, but your wounded leg gives out instantly.")
            print("A sharp, burning pain cuts through you like a blade and you let out a strained cry.")
            print("It’s enough.")
            print("The wolf’s head snaps toward you, its eyes locking onto you with feral hunger.")
            print("You glance around desperately — there’s only the fireplace poker within reach.")
            print("You drag yourself toward it, fingers brushing the cold metal, but the wolf is faster.")
            print("It crashes into you, slamming you to the floor. Its jaws clamp onto your shoulder, then your throat.")
            print("The pain is blinding. Your body weakens. Darkness closes in.")
            print("You should have treated your wound before trying to run.")
            print("GAME OVER")
            return
        else:
            print("After gathering your courage, you head to the kitchen cautiously.")
            print("On the far side of the kitchen, you see a large wolf sniffing the floor, searching for your scent.")
            print("You can see the door behind it standing open, that's how it followed you in.")
            print("That door might be your only way to escape.")
            print("But if you make any sudden movement, it might notice you.")

    # Final decisions
    print("----------------------------------")
    print("You freeze for a moment, heart pounding, as the wolf's gaze is fixed somewhere else.")
    print("This might be your only chance before it finally notices you.")
    print("As you run to the open door, you see a heavy kitchen knife on the counter by the way out.")

    decision_14 = input("Do you want to grab the knife or speedily run out? (Type 'KNIFE' or 'RUN') ")
    if decision_14.lower() == 'knife':
        knife_taken = True
    elif decision_14.lower() != 'run':
        invalid_choice()

    # 1) knife_taken
    if knife_taken:
        print("----------------------------------")
        print("You quickly grab the knife from the counter as you dash out the door.")
        print("The wolf growls madly and runs fast after you.")
        print("As you run for your life, the full moon looms over the horizon, casting long shadows behind you.")
    # 1.1.1) not car_was_destroyed + not injured_by_wolf + fuse_found + best_ending_achieved -> lives (best ending)
        if not car_was_destroyed:
            print("You see the car down the hill, this is your only chance to escape from this place.")
            if not injured_by_wolf:
                print("You feel a surge of adrenaline as you sprint away from the wolf.")
                print("You sprint as fast as you can toward your car, the knife clutched tightly in your hand.")
                print("As you enter the car and shut the door, the wolf reaches you, lunging itself against the window, determined to get to you.")
                print("The look in its eyes is filled with hunger and rage. You are terrified.")
                if fuse_found:
                    decision_15 = input("Do you lock the car door or reach for the fuse in your pocket? (Type 'LOCK' or 'FUSE') ")
                    if decision_15.lower() == 'fuse':
                        print("----------------------------------")
                        print("With the fuse you found earlier, you quickly replace it and manage to start the car.")
                        print("The wolf slams against the window, breaking it apart, but you are able to fend it off with the knife.")
                        print("You drive away as fast as you can, grateful to be alive.")
                        print("Through the rearview mirror, you see the wolf growling menacingly and plunging into the darkness.")
                        print("It was a close call, but you made it out alive.")
                        print("It will have to find another prey tonight.")
                        print("After a long drive, you finally reach your home safely.")
                        best_ending_achieved = True
    # 1.1.2) not car_was_destroyed + not injured_by_wolf + fuse_found + car_door_locked -> lives (full transformation ending)
                    elif decision_15.lower() == 'lock':
                        print("----------------------------------")
                        print("You quickly lock the car door, just as the wolf attacks ferociously the window.")
                        print("The wolf growls and slams the window again, and again, and this time it breaks it, attacking you.")
                        print("With the help of the knife, you fight bravely, fending off the wolf's attacks.")
                        print("You manage to injure it enough to make it retreat from your view.")
                        print("You quickly grab the fuse on your pocket and replace the blown one.")
                        print("With a turn of the key, the engine roars to life.")
                        print("But before you can drive away, the wolf lunges at you again, this time biting your arm as you try to fend it off.")
                        print("You manage to push it away with the knife, and speed off, but the bite is deep and painful.")
                        injured_by_wolf = True
                        print("You drive away from the house, grateful to be alive, but knowing you need urgent medical attention for your wound.")
                        print("After what seems like hours, you finally reach a hospital where you get treated for your injuries.")
                        first_aid_used = True
                        print("As you feel better, you drive back to the safety of your home. What a story to tell.")
                    else:
                        invalid_choice()
    # 1.1.3) not car_was_destroyed + not injured_by_wolf + no fuse_found -> dies
                else:
                    print("You run desperately to your car, your heart pounding in your chest.")
                    print("You didn't find a fuse earlier, so you know you won't be able to get the car started.")
                    print("But you hope that you can at least lock the doors and keep the wolf out.")
                    print("But this is not an ordinary wolf.")
                    print("It lunges at the window with incredible speed and strength, almost breaking it.")
                    print("With a terrifying growl, it smashes through the glass, its jaws snapping dangerously close to your face.")
                    print("You try to fend it off with the knife, but it's too strong.")
                    print("You battle fiercely, and with a powerful attack you cut it deeply on its face.")
                    print("The wolf howls in pain and retreats from your view, but you know it will be back.")
                    print("You desperately reach for the fuse box, hoping there was something you missed, but without a replacement fuse, the car will never start.")
                    print("The wolf returns, more furious than before, and jumps into the car, attacking you viciously.")
                    print("Despite your efforts to fend it off with the knife, it proves too strong for you.")
                    print("It bites you multiple times, leaving you unconscious. You succumb to your injuries.")
                    print("GAME OVER")
                    return
    # 1.1.4) not car_was_destroyed + injured_by_wolf + fuse_found -> lives (three possible endings: full transformation, ritual survival, partial cure)
            else:
                print("Despite the pain in your leg, you push yourself to run faster.")
                print("You clutch the knife tightly, ready to defend yourself if the wolf catches up.")
                print("But as you near your car, the wolf lunges at you, its jaws snapping dangerously close to your neck.")
                print("You manage to fend it off with the knife, cutting deeply into the beast's face.")
                print("The wolf howls in pain and retreats, giving you a chance to reach your car.")
                print("You throw yourself into the driver's seat, heart racing.")
                if fuse_found:
                    print("You reach for the fuse in your pocket and quickly replace the blown one.")
                    print("With a turn of the key, the engine roars to life.")
                    print("It's your chance to escape.")
                    print("But before you can press the gas, the wolf lunges at your window with all its strength.")
                    print("The scene terrifies you, freezing you in place for a moment.")
                    print("With a menacing growl, it smashes through the glass, trying to get to you again.")
                    print("As it tries to bite your neck, you cut straight at its previous injury, forcing the knife deep into its jaw.")
                    print("With a burst of strength, you shove its head back through the broken window and hit the gas, speeding off.")
                    print("You hear its howls as it chases you, but it soon falls behind, disappearing into the night.")
                    print("You drive as fast as you can to the nearest hospital. Though the bleeding on your leg was stopped, you know you need medical attention.")
                    print("After a tense and long drive, you finally see the lights of a hospital in the distance.")
                    print("They promptly treat your wounds, and as you feel better, you go back home.")
                    print("Nobody will believe such a tale.")
    # 1.1.5) not car_was_destroyed + injured_by_wolf + not fuse_found -> dies
                else:
                    print("You feel safe inside the car, but without a replacement fuse, there is no way to start it.")
                    print("In your mind you hope the wolf was too injured to try to attack you again.")
                    print("But as you breathe a sigh of relief, the wolf suddenly lunges at your window with all its strength, making you jump in fear.")
                    print("You can see the deep cut in its face bleeding, and the terror and rage in its eyes.")
                    print("It lunges itself against the window, its rage too great to ignore you.")
                    print("With a terrifying growl, it smashes through the glass, biting you fiercely on the shoulder.")
                    print("You try to fend it off with the knife, but it's too strong.")
                    print("After a terrible battle, the wolf overpowers you.")
                    print("It bites your neck ferociously, holding you firmly in its grasp.")
                    print("You feel your life slipping away as darkness engulfs you.")
                    print("GAME OVER")
                    return
    # 1.2.1) car destroyed + not injured_by_wolf -> dies
        else:
            print("With the car destroyed, you have no choice but to keep running.")
            if not injured_by_wolf:
                print("You manage to stay ahead of the wolf for a while, but eventually it catches up to you.")
                print("It ferociously lunges at you, throwing you to the ground.")
                print("You fight back with all your strength, using the knife to fend it off.")
                print("But the wolf is too strong, and it manages to grab your hand, biting down hard.")
                print("You scream in pain as it shakes its head violently, trying to tear your hand off.")
                print("You desperately cut at the wolf with the knife, piercing its side and leg.")
                print("The wolf howls in pain and finally releases you, retreating into the darkness.")
                print("But the damage is done. You are badly injured and bleeding heavily.")
                print('You arise weakly, trying to staunch the bleeding from your hand.')
                print("You know that there is nothing in the house that can help you now.")
                print("You keep running into the night, trying to find help before it's too late.")
                print("But you feel its presence behind you, and you know it will not give up the hunt so easily.")
                print("Despite your efforts to get away and find help, you are too tired and weak to keep going.")
                print("You reach a clearing near a river and you see a house on the other side.")
                print("You stumble towards it, hoping to find help.")
                print("But you will have to cross the river first, and you are too weak to swim.")
                print("As you collapse on the riverbank, the wolf appears behind you.")
                print("With a final, ferocious attack, it overpowers you.")
                print("You have no strength left to fight back, and you succumb to your injuries.")
                print("GAME OVER")
                return
    # 1.2.2) car destroyed + injured_by_wolf -> dies
            else:
                print("Your injured leg slows you down, as you run out of the house, and the wolf quickly catches up to you.")
                print("It lunges at you with terrifying speed, knocking you to the ground.")
                print("You try to fight back with the knife, but your strength is sapped from the earlier injury.")
                print("The wolf bites you fiercely on the neck, holding you firmly in its grasp.")
                print("As a last resource you stab the wolf in the eye with the knife, causing it to release you momentarily.")
                print("You cut at the wolf desperately again and again, as it howls in pain.")
                print("You feel the blood pouring from your neck, your vision blurring.")
                print("But you won't give up yet. You raise and try to run again, but the wolf is relentless.")
                print("It keeps at your back, biting you and then retreating from your attacks.")
                print("With each new attack the pain intensifies, and your strength fades.")
                print("You feel your life slipping away as darkness engulfs you.")
                print("The wolf is biding its time, waiting for you to weaken completely.")
                print("As your vision fades, you realize that this is the end.")
                print("You fall to the ground, watching helplessly as the wolf slowly closes in on you, waiting to savour your blood.")
                print("GAME OVER")
                return
    # 2) not knife_taken
    else:
        print("You decide to make a run for it as fast as you can.")
        print("The wolf notices you immediately and gives chase, its growls echoing through the night.")
        print("The full moon climbs the sky as you run, lighting the world too clearly — leaving you with nowhere to hide.")
    # 2.1) not knife_taken + not car_was_destroyed + not injured_by_wolf + fuse_found + not car_door_locked -> lives (full transformation ending)
        if not car_was_destroyed:
            print("You run as fast as you can to the car. It's the only way you can escape from this place.")
            if not injured_by_wolf:
                print("You feel a surge of adrenaline as you sprint away from the wolf.")
                print("You have to move fast as you have no way of defending yourself if it catches up.")
                print("As you shut the door the wolf reaches you, lunging itself against the door, your whole body jolts.")
                print("The beast takes a step back, readying to attack again. The look on its face is filled with hunger and rage.")
                print("You know that if it gets to you, it will rip you apart. You're terrified.")
                if fuse_found:
                    decision_15 = input("Do you lock the car door for safety or reach inside your pocket for the fuse? (Type 'LOCK' or 'FUSE') ")
                    if decision_15.lower() == 'fuse':
                        print("----------------------------------")
                        print("With the fuse you found earlier, you quickly manage to start the car.")
                        print("For a second, you almost forgot what is outside.")
                        print("The wolf slams powerfully against the window, breaking it apart, and biting your arm as you try to fend it off.")
                        print("You fight for your life trying to free your arm from its grasp. The knife would have been crucial now.")
                        print("In terror you pump at the gas and the car jumps, making the wolf release you momentarily.")
                        print("It's the opening you needed. You drive away as fast as you can, your arm limping with blood splattered across your body.")
                        injured_by_wolf = True
                        print("Through the rearview mirror, you see the wolf chasing you fiercely, but soon it disappears in the shadows.")
                        print("You need to get to an hospital quickly if you plan to stay alive.")
                        print("As you are about to collapse of the blood loss, you finally reach the hospital.")
                        print("They notice your dire condition, and quickly take you in for treatment.")
                        print("You are alive by a miracle.")
                        first_aid_used = True
                        print("After your condition is stable enough, you drive back home. The sun is going down, readying to set again.")
                        print("If you had heard this story from someone else, you wouldn't believe it.")
    # 2.2) not knife_taken + not car_was_destroyed + not injured_by_wolf + fuse_found + car_door_locked -> dies
                    elif decision_15.lower() == 'lock':
                        print("----------------------------------")
                        print("You instinctively lock the car door, just before one more attempt by the creature to break inside.")
                        print("You now feel safe inside the car.")
                        print("As you feel lulled by this false sense of safety, the wolf slams the window, this time breaking it.")
                        print("You try to fend it off as it bites your arms, trying to catch a grasp on your arm.")
                        print("Maybe the knife would be more effective at this point, had you decided to take it.")
                        print("You punch it as hard as you can, finally managing to hit its eyes, making it back off for a moment.")
                        print("You reach for the fuse on your pocket and quickly replace the blown one.")
                        print("But before you can turn the key, the wolf attacks through the broken window again, this time grabbing you by the neck.")
                        print("You punch it hard again, but you feel its teeth sinking deep into your neck.")
                        print("Your vision soon start to blurry as you feel the hot blood pouring from the deep wound.")
                        print("Your body starts to lose strength and soon you are plunged into darkness.")
                        print("Before you realize it, you succumb to your injuries.")
                        print("GAME OVER")
                        return
                    else:
                        invalid_choice()
    # 2.3) not knife_taken + not car_was_destroyed + not injured_by_wolf + not fuse_found -> dies
                else:
                    print("You run for your life, you know that the car is the only safe place to escape.")
                    print("You didn't find a fuse to start the car, but if you hide inside it until morning, the wolf surely will give up.")
                    print("As you lock the car door you look out the window you can't see the creature anymore.")
                    print("But it is too dark outside to see clearly. Maybe it just run away.")
                    print("For a few seconds you feel safe inside the car.")
                    print("Then, all of a sudden, it throws itself at the window with incredible strength, shacking the car.")
                    print("You try to not panic, as the window is between you two, it will not break, or so you think.")
                    print("With a terrifying growl, it throws itself against the glass, shattering it completely.")
                    print("The glass cuts your arms and face as you try to fend it off.")
                    print("You battle fiercely, but the wolf is simply too strong for you. If you had the knife, maybe you would have a chance to fight it.")
                    print("Finally it manages to grab your left arm almost ripping it off.")
                    print("You scream in pain, as you try to push yourself to the other side of the car to escape.")
                    print("But the wolf won't let you go, it plunges through the broken glass again and this time it grabs your neck, holding you firmly in its grasp.")
                    print("Despite your efforts to fight for your life, it proves too strong for you.")
                    print("You feel the terrible loss of blood, falling unconscious. There is no escape from this predator.")
                    print("GAME OVER")
                    return
    # 2.4) not knife_taken + not car_was_destroyed + injured_by_wolf -> dies
            else:
                print("Despite your best efforts, the wolf catches up to you.")
                print("You try to fend it off with your bare hands, but it's too strong.")
                print("It bite you harder than you can punch it back, trying to grab your neck for the final blow.")
                print("After what seems like an eternity it finally grabs straight to your shoulder, its teeth sinking deep in your flesh.")
                print("The wolf overpowers you, and your body starts to lose strength.")
                print("You see the mistake you made when you decide to not take that knife with you as your life withers away.")
                print("GAME OVER")
                return
    # 2.5) not knife_taken + car destroyed + not injured_by_wolf -> dies
        else:
            print("You look at the place where the car is still burning, there is no other option but to keep running.")
            if not injured_by_wolf:
                print("You run to the woods trying to outmaneuver the wolf.")
                print("It would be a terrible mistake to run in the open without a weapon to defend yourself.")
                print("As you enter the woods you look back and don't see the creature anymore.")
                print("Maybe you outsmarted it.")
                print("But as you turn around, it jumps from the shadows, throwing you against the trees.")
                print("It ferociously bites deep into your right arm, pulling you to the ground.")
                print("You fight back with all your strength, and manage to free your arm from its grasp.")
                print("But as you try to run again, it grabs your knuckle this time, and the pain throws you to the floor.")
                print("You scream in pain as it shakes you violently, and you kick it hard with your other leg, suddenly freeing you for a moment.")
                print("But the beast quickly lunges straight to your neck, biting it deep, its teeth cutting through your flesh.")
                print("You feel the hot blood pouring from your neck. You grasp for air, but there is none.")
                print("Soon darkness overpowers you and soon you are motionless.")
                print("GAME OVER")
                return
    # 2.6) not knife_taken + car destroyed + injured_by_wolf -> dies
            else:
                print("You feel the terrible pain slowing you down, as you run as fast as you can to the woods.")
                print("Down the road you can see the car in flames.")
                print("But before you can go too far from the house, the wolf reaches you.")
                print("Lunging at you with incredible strength and ferocity.")
                print("You fall to the ground hitting hard against a rock.")
                print("Before you can react the creature is over you biting your arms as you try to protect your face.")
                print("You quickly grab for the rock to try to fend it off, but it is too strong.")
                print("The wolf bites hard your left arm, pulling you violently, as you try to hit it with the rock.")
                print("Maybe that knife would have been a better choice, were you not in such a haste to run.")
                print("As your arm limp to the side, the wolf lunges on your neck, cutting a deep wound.")
                print("You feel the world spinning around you and everything goes dark.")
                print("The only thing you see is the monster coming over you as it finally grab you by the neck.")
                print("GAME OVER")
                return

    # 1. Best Ending:
    if best_ending_achieved:
        print("As you lie down on your bed and glance out the window, you see the full moon rising over the horizon.")
        print("You can't help but wonder what that creature truly was. Too large, too fierce, too deliberate to be a simple wolf.")
        print("But you push the thought aside. There is much to do tomorrow, and you need to rest for now.")
        print("One thing is certain: you' a're never taking that road again.")
        print("If you had chosen differently that night, would your life be the same now?")
        print("There is no way to know.")
        print("Or is there?")
        print("Sometimes the road you escaped keeps calling you back.")
        print("----------------------------------")
        print("THE END")
        return

    # 2. No transformation... kind off:
    elif salve_used:
        print("The days after your escape pass almost normally.")
        print("The wound heals cleanly, leaving no trace of the terror you lived through.")
        print("But as the next full moon approaches, something in you begins to stir.")
        print("On the night it rises again, you feel an invisible pull drawing you outside.")
        print("You sit on your rocking chair on the porch, watching its first golden rays shine on the horizon.")
        print("Then it begins.")
        print("Suddenly, distant sounds seem sharper. As if your hearing has come alive.")
        print("You can hear insects in the grass, wings fluttering in the trees, even the soft pulse of your own heartbeat.")
        print("You can smell every living thing moving around your home.")
        if amulet_found:
            print("Then you hear it, a voice muttering to itself about rabbits it plans to chase in the woods.")
            print("You turn your head just in time to see your neighbor's dog trotting past your house.")
            print("It notices you and freezes. Staring at you as if recognizing you as one of its own.")
            print("Then it nods, and wander off, still mumbling about its hunt.")
            print("You shake your head, blaming your imagination for the strange effects you are experiencing.")
            print("Instinctively, you reach into your pocket... feeling that amulet you found in the woods.")
            print("There are strange letters written on it, shimmering in the moon light, though their meaning is unknown to you.")
        else:
            print("Strange muffled sounds drift from around the corner, but you can't clearly understand what it is saying.")
            print("A moment later, that dog who lives on the next house appears, strolling past your porch.")
            print("It then pauses, staring at you with unusual familiarity, as if you were old friends.")
            print("Then it moves on, tail swaying, disappearing towards the woods.")
        print("As the moon climbs higher - full, bright, almost golden - you feel a deep hunger awaken inside you.")
        print("A craving for raw meat. Fresh, warm, dripping... nothing else seems to satisfy.")
        print("You force the thought away, disturbed by how natural it felt.")
        print("Days pass, and the cravings worsen. Cooked food tastes like paper. Only raw mear feels 'right'.")
        print("Soon, local dogs begin appearing at your property more often, drawn to you for reasons you can't explain.")
        if amulet_found:
            print("You notice that whenever the amulet is near you, something strange happens: you can understand your canine visitors perfectly.")
            print("Their voices echo in your mind as if whispered directly into your thoughts.")
        print("But the strangest: your senses heighten dramatically every full moon.")
        print("Under the moonlight, you feel an urge growing stronger with each cycle: to run through the woods.")
        print("To shed your clothes and feel the fresh air in your naked skin.")
        print("To hunt something alive... to feel it struggle between your teeth.")
        print("But you resist.")
        print("Life goes on - strange, but still your own.")
        print("Though you can't stop wondering: which choices on that fated night made you become like this?")
        print("...")
        print("Yet every night, as the moon rises, the same question returns:")
        print("'What choices did I make on that cursed night that led me here?'")
        print("'Could my fate have been different?'")
        print("----------------------------------")
        print("THE END")
        return

    # 3. Full transformation:
    elif first_aid_used:
        print("Though the hospital staff treated your injuries and sent you home with painkillers, something feels wrong inside you.")
        print("As if something is crawling beneath your skin, restless and alive.")
        print("Days pass. You try to ignore the unease building inside.")
        print("But when the next full moon is about to rise, something calls you outside.")
        print("As the last traces of sunset fade away, a cool breeze brushes your skin, carrying distant voices in the wind.")
        print("Your gaze drifts toward the horizon. It is coming. The time has arrived.")
        print("As the first rays of the moonlight spill across the sky, it begins.")
        print("Your skin burns, hot and feverish. Sweat runs down your brow in heavy streams.")
        print("Your heartbeat pounds in your ears, each thump louder than the last. ")
        print("Every sound around you stabs into your skull like needles.")
        print("You stagger through the corridor toward the door. You desperately need fresh air.")
        print("As you step outside, you see the full moon rising: huge, bright, merciless. And the change begins.")
        print("Your nails lengthen, black and curved. Your tear your shirt apart, gasping for breath.")
        print("Hair erupts across your arms, your spine, your face. You canines push outward, tearing through your gums.")
        print("Your jaw cracks, reshaping itself with sickening pops.")
        print("Every bone in your body shifts, breaks, reforms. The pain is overwhelming.")
        print("You collapse, screaming… and then snarling. Terror floods you as your mind slips, trying to make sense of what you are becoming.")
        print("Your senses explode with unnatural clarity:")
        print("You smell every living creature moving around the house, each scent sharp and unmistakable.")
        print("You hear voices in the distance - not human voices, but your canine companions whispering to the night and to the moon.")
        print("Your vision slices through the darkness as if it were daylight, but the colors bleed away.")
        print("Reds sink into shadow. Greens fade to yellow. But blues burn like tiny moons scattered across the world.")
        print("The world makes the most sense only when it moves; every twitch pulses with life..")
        print("The night hides nothing from you now.")
        print("But above all else, a hunger rises inside you - deep, ancient, inescapable.")
        print("A hunger that devours thought, memory, and restraint.")
        print("You crave the hunt. You crave warm flesh struggling between your teeth. You crave blood and human flesh.")
        print("With a guttural snarl, you tear out of your last rags and sprint into the night.")
        print("Back to the forest.")
        print("Back to where it all began.")
        print("Following the scent that started this curse.")
        print("The rest becomes a blur… a nightmare written in blood and moonlight.")
        print("And you are no longer human to tell the tale.")
        print("----------------------------------")
        print("THE END")
        return

    # Secret ending:
    # 4. No transformation... for now (ritual ending):
    elif coal_used:
        print("You finally return home from the hospital, exhausted but alive.")
        print("As you sit down on your rocking chair on the porch under the moonlight, something pokes you.")
        print("You reach into your back pocket — and there it is.")
        print("The amulet you found in the forest.")
        print("You unwrap it, feeling the curved tooth warm against your skin.")
        print("Strange markings etched along the enamel seem to shimmer under the light.")
        print("As if by instinct, you reach for the old diary you carried from the cabin.")
        print("For some unknown reason, the strange, rough handwriting now makes sense to you.")
        print("Some pages are stained with dirt… or dried blood.")
        print("You read the first page.")
        print("'This curse is older than the forest.")
        print("Older than the monster that hunted me…")
        print("And that now I hunt.'")
        print("A chill runs through you, as you uncover the truth.")
        print("Long ago, the land belonged to a native tribe.")
        print("Their chief had a daughter — the most beautiful of all, the pride of her people.")
        print("A jealous man desired her, but the chief refused him.")
        print("So one late evening, the man followed her into the forest as she picked berries.")
        print("He assaulted her and, in panic, spilled her blood as the full moon was rising.")
        print("Fearing punishment, he dragged her body deep into the woods, hoping wolves would devour the evidence.")
        print("And so they did.")
        print("But the dark spirits of the forest saw everything, and rejoiced in the foul deed.")
        print("When the tribe searched for her, all they found were torn garments.")
        print("They had no way to know which lair her body had been taken to, for the wolves kept many across the region.")
        print("When the truth finally surfaced, the man was found and dragged before the chief.")
        print("But the chief did not kill him, as was the custom.")
        print("In his grief, he cursed the man.")
        print("'You took what was sacred and spilled innocent blood —")
        print("may you now roam with the beasts until her bones are found and my heart is laid to rest.'")
        print("Words spoken in anguish and rage… though never meant to be magic.")
        print("But the spirits twisted them into something real — and terrible.")
        print("The man fled into the forest, dark voices screaming curses around him.")
        print("And when the moonlight touched him, he transformed.")
        print("Thus, the first werewolf was born — and a trail of blood followed it.")
        print("The wolf grew monstrous with each kill, swollen with unnatural strength from tasting human blood.")
        print("But as that first moon set, it hid in its lair, biding its time.")
        print("Each full moon, it hunted the tribe, feeding on their fear — and their flesh.")
        print("'We thought hunting the beast would be easy.")
        print("But we were wrong.'")
        print("Rarely did its victims survive.")
        print("And those who did transformed at the next full moon — weaker, confused, but deadly.")
        print("They all shared one instinct:")
        print("To hunt the alpha and take its place, fighting to the death.")
        print("Thus the older beast grew only stronger — feeding on the newborn werewolves.")
        print("Becoming almost impossible to kill.")
        print("Still, the tribe tried.")
        print("They learned it could not be harmed under the moonlight.")
        print("So they waited, hunting it at its weakest, when it hid in its lairs.")
        print("Outside the full moon, it appeared as any other wolf — though larger, fiercer, leading its pack.")
        print("Through trial and loss, the chief created a salve.")
        print("If applied immediately after a bite, while the blood was still warm, it halted the transformation.")
        print("'The salve keeps the curse from rooting,")
        print("but it does not erase it.'")
        print("Those healed developed strange, beast-like behaviors… until they eventually succumbed to madness.")
        print("The only true cure was to find the remnants of the chief’s daughter — so her spirit could finally rest.")
        print("Only then would the spirits of the forest be appeased.")
        print("But they never succeeded.")
        print("The beast had hidden her bones in one of its many lairs and guarded them fiercely.")
        print("But the chief had vowed to kill the creature and free his people from its torment.")
        print("After years of tracking, they finally discovered one of its hiding places.")
        print("On the morning before the full moon, they set the area ablaze and stormed the den.")
        print("They fought bravely. Many died.")
        print("Even in its weakest form, the beast was terrifying.")
        print("But at last they killed it — cutting off its head as a trophy.")
        print("They used the last remaining salves to heal the bitten and began the journey home.")
        print("Only when the adrenaline faded did the truth strike them:")
        print("The chief had been bitten.")
        print("He pulled a tooth from the deep wound, blood pouring freely.")
        print("But there was no salve left… nor time to make a new one, and the sun was already sinking.")
        print("In desperation, he sought the spirits’ help.")
        print("The tribe could hear their terrifying screams in the forest.")
        print("He carved sacred symbols into the tooth and drew a circle of ash around himself.")
        print("With his own blood, he inscribed runes across the circle.")
        print("At the exact moment the moon’s first rays touched him, he began the chant.")
        print("His body trembled and shook.")
        print("The spirits answered —")
        print("and the ritual halted the transformation.")
        print("But the spirits were liars.")
        print("They never revealed the full price.")
        print("'We rejoiced too soon.")
        print("The ritual must be repeated every full moon,")
        print("at the same place,")
        print("at the same moment.'")
        print("On the next full moon, he transformed —")
        print("killing half his remaining tribe before dawn.")
        print("'The chief discovered this only when it was too late,")
        print("and now the curse flows freely again.'")
        print("The tribe hunted down the new beast.")
        print("And the cycle began again.")
        print("Every bitten slowly descended into madness, or became a new guardian…")
        print("Performing the ritual until they failed — or died in the hunt.")
        print("The tribe dwindled and finally moved away.")
        print("But neither the wolf nor the cursed keepers could leave the land.")
        print("The ritual bound them to that place.")
        print("And the beast was chained by instinct — compelled to guard the bones that could end its curse.")
        print("As generations passed, their story faded into myth.")
        print("None remembered the truth except the guardian — and he wrote it all within these pages.")
        print("When you reach the final page, your hands tremble.")
        print("A final message is scrawled in desperate handwriting:")
        print("'If you are reading this…")
        print("it means I failed, and the curse has chosen you next.")
        print("At least now you know what must be done to end it.'")
        print("The room grows colder.")
        print("That night, you return to the cabin.")
        print("The forest feels different now — familiar in a way that terrifies you.")
        print("You wait for the next cycle, preparing yourself for the ritual.")
        print("When the moment finally arrives, you draw the circle and the runes on the sacred spot.")
        print("You spill the blood. You whisper the chants.")
        print("And when the moon rises, your body pulses —")
        print("the curse pushing, twisting, trying to claim you.")
        print("You hear the spirits of the forest laughing, cursing you.")
        print("Your bones burn.")
        print("Your heart races.")
        print("Your senses sharpen.")
        print("A hunger stirs in your veins.")
        print("Your instincts hum with predatory impulse.")
        print("But the circle holds.")
        print("You remain human.")
        print("Almost. You are not the same.")
        print("But your mind is your own.")
        print("You survived this moon.")
        print("Next month, you must do it again.")
        print("And the month after.")
        print("And after.")
        print("Until you kill the wolf that bit you.")
        print("Until you follow its scent back to its lair.")
        print("Until you find the bones of the chief’s daughter.")
        print("Until the curse is broken.")
        print("You watch silently as the moon reaches its peak.")
        print("Somewhere in the shadows, you feel the presence of the beast.")
        print("Your eyes pierce the darkness with unnatural clarity, searching for it.")
        print("It does not attack.")
        print("It senses you as one of its own — not prey, nor a monster.")
        print("For now, you are safe.")
        print("But will it feel the same when you become its hunter?")
        print("----------------------------------")
        print("THE END")
        return
    else:
        print("ERROR! ERROR! ERROR!")

while True:
    play_game()
    print("----------------------------------")
    print("You come to the final of the story.")
    replay = input("Would you like to play it again? (Type 'YES' or 'NO') ")
    if replay.lower() == 'no':
        print("Thanks for playing!")
        print("----------------------------------")
        break
    elif replay.lower() == 'yes':
        continue
    else:
        invalid_choice()