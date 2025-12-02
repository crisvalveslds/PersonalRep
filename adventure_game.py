# Adventure Game -- Cristiano Alves
# I was very happy to create this game as I love this kind of horror stories that are interactive.
# I asked a friend and my daughter to play the game and they really enjoyed the story and the multiple choices you can make.
# I plan to add more small tweaks to this game in the future and expand it a bit more, maybe even convert it into a playable mini-game.
# This game takes through the events of a special full moon night.
# You can play this multiple times for the different outcomes and especially for the 4 different endings.

import sys
import time

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
    got_umbrella = False

    typewriter_print(
        "----------------------------------\n"
        "Welcome to the Adventure Game!\n"
        "----------------------------------\n"
        "The forest road stretches endlessly ahead, swallowed by darkness.\n"
        "You shouldn't have taken this shortcut.\n"
        "That stranger at the gas station seemed so certain it would save you time.\n"
        "But you've been driving for nearly an hour without seeing a single other car.\n"
        "Just trees. Endless trees pressing close to the narrow road.\n"
        "The sky above is caught in that strange twilight between day and night.\n"
        "The last traces of sunset have faded, but the moon hasn't risen yet.\n"
        "Not that it matters — you just need to get home.\n"
        "A warning light suddenly flickers on the dashboard — you don't recognize the symbol.\n"
        "Before you can check what it means, the engine coughs.\n"
        "Once.\n"
        "Twice.\n"
        "Then it dies completely, and the car rolls to a silent stop.\n"
        "You try the ignition. Nothing happens. Not even a click.\n"
        "The headlights dim, then go dark.\n"
        "Your phone — you grab it immediately, but your heart sinks.\n"
        "No signal. And the battery is at 3%.\n"
        "Of course. You forgot to charge it this morning.\n"
        "You're on your own.\n"
        "In the sudden silence, you become aware of how alone you are.\n"
        "How far from anything.\n"
        "How dark it is out here.\n"
        "\nWill you try starting the car again or check the owner's manual in the glove box? (Type 'START' or 'MANUAL') "
    )

    # First circle of decisions
    decision_1 = input("")
    if decision_1.lower() == 'start':
        typewriter_print(
            "----------------------------------\n"
            "You turn the key firmly.\n"
            "The engine makes a weak, grinding sound — like something trying and failing to catch.\n"
            "A faint clicking starts somewhere under the dashboard.\n"
            "Rhythmic. Mechanical. Almost like a countdown.\n"
            "The warning light flickers weakly, then dies again.\n"
            "You wait, listening to the clicking, trying to understand what it means.\n"
            "Outside, the wind picks up, rustling through the branches.\n"
            "The darkness is deepening. Soon it will be pitch black out here.\n"
            "You glance through the windshield, peering into the treeline.\n"
            "Far off, maybe thirty yards into the forest, something moves between the trees.\n"
            "Just a shift in the shadows. Could be a deer.\n"
            "Could be nothing.\n"
            "You blink, and whatever it was has stopped moving.\n"
            "The clicking under the dashboard continues its steady rhythm.\n"
            "You need to figure this out before it gets any darker.\n"
            "\nDo you try starting the car again or check under the dashboard for that clicking sound? (Type 'START' or 'DASHBOARD') "
        )
        decision_2 = input("")
        if decision_2.lower() == 'start':
            typewriter_print(
                "----------------------------------\n"
                "You grip the key and twist it hard, putting your weight behind it.\n"
                "The engine shudders violently this time, metal grinding against metal somewhere deep inside.\n"
                "The clicking under the dashboard accelerates — faster, more urgent.\n"
                "A sharp smell cuts through the stale car air.\n"
                "Burnt plastic. Hot metal. Something electrical overheating.\n"
                "The warning light flares bright red for a split second, flooding the car interior with bloody light.\n"
                "In that brief flash, you catch movement through the passenger window.\n"
                "Closer now. In the bushes just off the road. Maybe ten feet away.\n"
                "The light dies, plunging you back into darkness.\n"
                "You hold your breath, straining to hear.\n"
                "The bushes rustle. Something moving through them.\n"
                "Not the wind. Too deliberate. Too low to the ground.\n"
                "An animal, probably. A fox. Maybe a raccoon.\n"
                "But the rustling moves along the side of the car. Following the length of it.\n"
                "Your heart starts to beat faster.\n"
                "The engine was *so close* to catching — you felt it shudder, trying to turn over.\n"
                "If you could just force it... just one more push...\n"
                "But that burning smell is getting stronger.\n"
                "And whatever's in those bushes is getting closer to your door.\n"
                "\nDo you try forcing the engine one more time or get out and look for help? (Type 'TRY' or 'HELP') "
            )
            decision_3 = input("")
            if decision_3.lower() == 'try':
                typewriter_print(
                    "----------------------------------\n"
                    "You can't go out there. Not with that thing so close.\n"
                    "You just need the engine to start. Just once.\n"
                    "You turn the key with everything you have.\n"
                    "The engine screams — a tortured, mechanical shriek.\n"
                    "The clicking becomes a frantic staccato. Smoke curls from the dashboard.\n"
                    "**No no no**\n"
                    "Outside, the rustling stops.\n"
                    "Then you hear it step onto the gravel.\n"
                    "Heavy. Deliberate. Paws, not hooves.\n"
                    "Each footfall crunches with a weight that makes your stomach drop.\n"
                    "It circles around the back of your car. Then up the passenger side.\n"
                    "You track it by sound alone, barely breathing.\n"
                    "It stops at your door.\n"
                    "You hear breathing. Deep. Rhythmic. Right outside your window.\n"
                    "So close the glass fogs with each exhale.\n"
                    "Something scrapes against the door — claws testing the surface.\n"
                    "A low rumble emanates from its chest. Not quite a growl. Something deeper.\n"
                    "The warning light explodes into blinding brightness—\n"
                    "Then everything goes black.\n"
                    "A dull *whoomph* from under the hood.\n"
                    "Orange light. Heat against your face.\n"
                    "**Fire.**\n"
                    "The creature bolts — crashing through underbrush, fleeing the flames.\n"
                    "You throw yourself out as fire erupts across the engine.\n"
                    "The heat chases you back. You stumble away, watching your only escape burn.\n"
                    "The flames roar higher, casting wild shadows through the trees.\n"
                    "Whatever it was, it fled from the fire.\n"
                    "As you catch your breath, you notice something near your door.\n"
                    "Deep gouges in the gravel. And pressed in the soft dirt: a print.\n"
                    "Large. Canine. But far too big for any dog.\n"
                    "Four toes. Claws extending at least an inch beyond the pads.\n"
                    "You need shelter. Now.\n"
                    "Through the smoke, you spot a faint glow in the distance on a hill.\n"
                    "A house.\n"
                    "It's your only chance.\n"
                )
                car_was_destroyed = True
            elif decision_3.lower() == 'help':
                typewriter_print(
                    "----------------------------------\n"
                    "Your hand freezes on the key.\n"
                    "The smell. The clicking. That animal in the bushes.\n"
                    "This is wrong. All of it.\n"
                    "You need to get out — now — before the car fails completely.\n"
                    "Before whatever's out there gets any closer.\n"
                    "Your hand reaches back and grabs the first thing it finds on the rear seat.\n"
                    "An umbrella. The heavy one with the wooden handle.\n"
                    "It's not much, but it's better than nothing.\n"
                    "You take a breath, steel yourself, and push the door open slowly.\n"
                    "The dome light doesn't come on — the electrical system is dying.\n"
                    "Good. You don't want to be visible.\n"
                    "As you step onto the gravel, you freeze.\n"
                    "You hear it clearly now.\n"
                    "Sniffing. Deep, deliberate breaths. Right behind your car.\n"
                    "Whatever it is, it's large. You can hear the weight of it shifting on the gravel.\n"
                    "The sniffing moves along the back bumper, then down the passenger side.\n"
                    "It's tracking your scent.\n"
                    "You can't see it — it's too dark, and it's staying low.\n"
                    "But it's there. Right there.\n"
                    "Your fingers tighten on the umbrella handle.\n"
                    "Slowly, carefully, you edge around to the front of the car.\n"
                    "You pop the hood as quietly as possible — it hisses softly as it opens, releasing a thin wisp of smoke.\n"
                    "The engine looks intact, but there's a scorch mark near the battery.\n"
                    "Close. Too close to a fire.\n"
                    "The sniffing has stopped.\n"
                    "Silence.\n"
                    "That's somehow worse.\n"
                    "You crouch by the driver's door and find the fuse panel under the dashboard.\n"
                    "Your hands shake as you check it.\n"
                    "One fuse has blown completely — glass blackened, metal melted.\n"
                    "The fuel pump fuse.\n"
                    "If you'd kept forcing the ignition, it would have caught fire.\n"
                    "Without a replacement, the car is dead.\n"
                    "A twig snaps somewhere behind you.\n"
                    "You don't turn around. You don't want to know how close it is.\n"
                    "You just start walking.\n"
                    "Fast.\n"
                    "Ahead, through the trees, you spot a narrow path leading uphill.\n"
                    "At the top, barely visible, a light glows through the branches.\n"
                    "A house.\n"
                    "You grip the umbrella tighter and head toward it, forcing yourself not to run.\n"
                    "Not yet.\n"
                )
                got_umbrella = True
            else:
                invalid_choice()
        elif decision_2.lower() == 'dashboard':
            typewriter_print(
                "----------------------------------\n"
                "You lean down, pressing your ear close to the dashboard.\n"
                "The clicking is rhythmic, mechanical — like a relay switch stuck in a loop.\n"
                "Definitely electrical, not the engine itself.\n"
                "That's... something, at least. You can work with electrical.\n"
                "The sky outside is getting darker. The last traces of twilight are fading fast.\n"
                "You need to work quickly.\n"
                "You feel around under the dashboard for the fuse panel, squinting in the dim light.\n"
                "The plastic cover pops off easily, revealing rows of colored fuses.\n"
                "As you examine them, you hear rustling outside.\n"
                "In the bushes. Closer than before — maybe eight or ten feet from the passenger side.\n"
                "You freeze, listening.\n"
                "Something's moving through the undergrowth. Low to the ground.\n"
                "The rustling stops. Then starts again, moving parallel to the car.\n"
                "An animal. Has to be.\n"
                "Probably foraging. Maybe curious about the car.\n"
                "You turn your attention back to the fuses.\n"
                "There — one of them has blown. Blackened glass, melted connector.\n"
                "The fuel pump fuse.\n"
                "That explains everything. The clicking was the relay trying to activate a dead circuit.\n"
                "If you'd kept forcing the ignition, you might have caused a short circuit. Maybe worse.\n"
                "But without a replacement, the car won't start.\n"
                "Outside, the rustling has moved to the bushes behind the car.\n"
                "Closer. More deliberate.\n"
                "You need to move.\n"
                "As carefully as possible, you ease the door open and slip out.\n"
                "Ahead, through the trees, you see a faint light on a hillside.\n"
                "A house. Someone who can help.\n"
                "You start walking, glancing back at the bushes.\n"
                "Whatever was there has gone quiet.\n"
                "That doesn't make you feel better.\n"
            )
        else:
            invalid_choice()
    elif decision_1.lower() == 'manual':
        typewriter_print(
            "----------------------------------\n"
            "You pop open the glove box and grab the owner's manual.\n"
            "The pages feel stiff — you've never needed this before.\n"
            "You flip to the index, searching for warning lights.\n"
            "There: 'Warning Lights and Indicators'\n"
            "You scan down until you find the symbol.\n"
            "'Fuel System Malfunction — Check Fuse Panel Immediately. Do Not Attempt Restart.'\n"
            "A diagram shows the fuse panel location under the dashboard.\n"
            "You set the manual aside and feel for the panel in the growing darkness.\n"
            "The twilight is fading fast. Soon it will be completely dark.\n"
            "The panel clicks open, and you lean down to examine the fuses.\n"
            "One has clearly blown — glass blackened, connector melted.\n"
            "The fuel pump fuse.\n"
            "The manual's warning was serious: 'Attempting to start engine with this fuse blown may cause electrical fire.'\n"
            "You made the right call.\n"
            "But you're still stranded.\n"
            "As you sit back, you glance through the windshield.\n"
            "Far off in the forest, maybe thirty or forty yards out, you notice movement.\n"
            "Just a shifting shadow between the trees.\n"
            "Could be anything. A deer. The wind.\n"
            "It's too dark to make out clearly.\n"
            "Whatever it is, it's not your immediate problem.\n"
            "You need to find help.\n"
            "You step out carefully, scanning the area.\n"
            "Through the branches ahead, you spot a faint glow on a hillside.\n"
            "A house. Lights in the windows.\n"
            "That's where you need to go.\n"
            "You start toward it, walking steadily.\n"
            "Behind you, something moves through the forest.\n"
            "Distant. Following.\n"
            "You keep walking.\n"
        )
    else:
        invalid_choice()

    # Second circle of decisions
    typewriter_print(
        "----------------------------------\n"
        "As you start up the hill toward the house, the first rays of moonlight break over the horizon.\n"
        "The moon rises full and bright, casting long silver shadows through the trees.\n"
        "The wind picks up, howling through the branches.\n"
        "You pull your jacket tighter and keep moving.\n"
        "Then you hear it — a sound from the woods to your left.\n"
        "Not an animal sound.\n"
        "Someone gasping. Struggling for breath.\n"
        "It sounds like... pain. Raw, desperate pain.\n"
        "A choked cry cuts through the wind, almost human.\n"
        "Then a wet, cracking sound.\n"
        "Another gasp — this one deeper, more guttural.\n"
        "Someone's hurt.\n"
        "\nSomeone might need help. Do you investigate or continue to the house? (Type 'INVESTIGATE' or 'HOUSE') "
    )
    decision_4 = input("")
    if decision_4.lower() == 'investigate':
        typewriter_print(
            "----------------------------------\n"
            "You turn toward the trees, moving carefully down the slope.\n"
            "The sounds are coming from somewhere in the dense undergrowth.\n"
            "Another gasp — wet, labored, like someone drowning in their own breath.\n"
            "Then a low moan that makes your skin crawl.\n"
            "It starts human but trails off into something else.\n"
            "\"Hello?\" you call out. \"Are you hurt? Do you need help?\"\n"
            "The sounds stop abruptly.\n"
            "Complete silence.\n"
            "The moonlight filters through the branches, casting everything in sharp silver and shadow.\n"
            "You hear movement now — something shifting in the darkness.\n"
            "Heavy. Uneven. Like someone crawling.\n"
            "Then that wet cracking sound again. Louder. More violent.\n"
            "A strangled whimper that could be pain... or something else.\n"
            "You can't see anything yet. Just the shifting shadows between the trees.\n"
            "But something tells you this isn't right.\n"
            "\nThe sounds have stopped. Do you keep searching or head back? (Type 'SEARCH' or 'BACK') "
        )
        decision_5 = input("")
        if decision_5.lower() == 'search':
            typewriter_print(
                "----------------------------------\n"
                "You push forward, stepping over roots and through tangled brush.\n"
                "You need to know. Someone might be dying out here.\n"
                "Then you see it.\n"
                "Fabric. A torn piece of cloth snagged on a low branch.\n"
                "Dark. Could be a shirt. Or a jacket.\n"
                "You touch it — still warm.\n"
                "A few steps further, another piece. Larger this time. Shredded.\n"
                "Not cut. Torn.\n"
                "Like someone ripped their clothes off in a frenzy.\n"
                "Your pulse quickens.\n"
                "More pieces litter the ground now. A trail of them.\n"
                "Buttons. Scraps of fabric. A shoe, overturned in the dirt.\n"
                "The moonlight filters through the branches, making everything look silver and strange.\n"
                "As you round a thick cluster of trees, an owl suddenly explodes from above.\n"
                "You cry out, stumbling backward, heart hammering.\n"
                "The owl's shriek echoes through the forest, then fades.\n"
                "In the silence that follows, you hear it again.\n"
                "Breathing. But wrong.\n"
                "Too deep. Too wet. Each exhale a rattling growl.\n"
                "The cracking sounds have stopped. Whatever was happening... it's finished.\n"
                "The clothing trail ends here. Just... stops.\n"
                "But something else is ahead.\n"
                "Moving. Not crawling anymore. Not struggling.\n"
                "Moving with purpose.\n"
                "You feel it before you see it — the weight of its attention.\n"
                "A cold breeze cuts through the trees, carrying a smell.\n"
                "Something strangely familiar.\n"
                "\nEvery instinct screams danger. Do you continue or run? (Type 'CONTINUE' or 'RUN') "
            )
            decision_6 = input("")
            if decision_6.lower() == 'continue':
                typewriter_print(
                    "----------------------------------\n"
                    "You take one more step forward, pushing aside a low branch.\n"
                    "That's when you see them.\n"
                    "Eyes. Glowing in the moonlight.\n"
                    "Yellow-green, bright as lanterns, staring directly at you.\n"
                    "They're low to the ground. Wide set. Unblinking.\n"
                    "Your breath catches in your throat.\n"
                    "The shape around those eyes begins to resolve in the shadows.\n"
                    "Massive. Far larger than any wolf should be.\n"
                    "Its shoulders are level with your chest, even on all fours.\n"
                    "The moonlight catches its fur — dark, bristling, almost black.\n"
                    "Its lips pull back slowly, deliberately.\n"
                    "Teeth. So many teeth. Each one as long as your thumb.\n"
                    "A low growl builds in its chest — not the sound you heard before.\n"
                    "This is pure, predatory threat.\n"
                    "This is no injured person. This was never a person.\n"
                )
                if got_umbrella:
                    typewriter_print(
                        "Your hand tightens on the umbrella.\n"
                        "You raise it instinctively, putting it between you and the creature.\n"
                        "The beast's eyes track the movement.\n"
                        "Its growl intensifies, and you realize how utterly inadequate this is.\n"
                        "An umbrella. Against that.\n"
                    )
                
                typewriter_print(
                    "As you slowly back away, your foot catches on something.\n"
                    "You glance down for just a split second.\n"
                    "There, half-buried in the leaves: a long, curved tooth.\n"
                    "Old. Yellowed. Scratched with faint markings you can't read.\n"
                    "A thin strip of leather is wrapped around its base.\n"
                    "Your eyes snap back to the creature. It hasn't moved.\n"
                    "But its muscles are coiled. Waiting.\n"
                    "\nDo you pick up the tooth or leave it? (Type 'PICK' or 'LEAVE') "
                )
                
                decision_7 = input("")
                if decision_7.lower() == 'pick':
                    typewriter_print(
                        "----------------------------------\n"
                        "You snatch the tooth and shove it into your pocket.\n"
                        "Your eyes never leave the creature.\n"
                        "Its growl deepens. It doesn't like that you took it.\n"
                        "You back away slowly, one step at a time.\n"
                        "The beast shifts its weight forward.\n"
                    )
                    amulet_found = True
                elif decision_7.lower() == 'leave':
                    typewriter_print(
                        "----------------------------------\n"
                        "You step carefully over the tooth, not daring to look away.\n"
                        "Survival. That's all that matters.\n"
                        "You back away slowly, one step at a time.\n"
                        "The beast's eyes follow your every movement.\n"
                    )
                else:
                    invalid_choice()
                
                typewriter_print(
                    "Then it happens.\n"
                    "The creature lunges.\n"
                    "Impossibly fast. A blur of fur and teeth.\n"
                )
                
                if got_umbrella:
                    typewriter_print(
                        "You swing the umbrella wildly as you turn to run.\n"
                        "It flies from your hands, clattering uselessly against the trees.\n"
                    )
                
                typewriter_print(
                    "You run.\n"
                    "Every ounce of strength, every bit of will, focused on reaching that house.\n"
                    "You burst from the trees, sprinting up the hill.\n"
                    "The door — you can see it — just ahead—\n"
                    "You hit the porch at full speed and throw yourself at the door.\n"
                    "It gives way and you crash inside.\n"
                    "Behind you, the creature is right there—\n"
                    "Its jaws snap shut around your left leg.\n"
                    "Teeth sink deep into muscle.\n"
                    "You scream and kick with your other leg, catching it square in the muzzle.\n"
                    "It releases for just a moment — enough.\n"
                    "You throw your weight against the door.\n"
                    "It slams shut just as the creature lunges again.\n"
                    "The door shudders. Once. Twice. Three times.\n"
                    "Then... silence.\n"
                    "You collapse against the wall, gasping.\n"
                    "Your leg is on fire. Blood soaks through your pants.\n"
                    "When you look down, you see it clearly:\n"
                    "Deep puncture wounds. Four on top. Four on bottom.\n"
                    "Perfectly symmetrical. Impossibly large.\n"
                )
                injured_by_wolf = True
                
                if car_was_destroyed:
                    typewriter_print(
                        "----------------------------------\n"
                        "You tear off your shirt with shaking hands, wrapping it around your leg.\n"
                        "The fabric soaks through immediately. Dark. Too dark.\n"
                        "You pull it tighter, gasping at the pain, but the bleeding won't stop.\n"
                        "Your vision blurs at the edges. The room tilts.\n"
                        "The car is gone. Burned. There's no escape.\n"
                        "You're trapped in this house with a monster outside and a wound that might kill you before it does.\n"
                        "You need help. Real help. Medicine. Something.\n"
                        "Or you're going to die here.\n"
                    )
                else:
                    typewriter_print(
                        "----------------------------------\n"
                        "You rip off your shirt and bind it around your leg, pulling the knot tight.\n"
                        "The pain is blinding. White-hot. You taste copper in your mouth.\n"
                        "Blood seeps through the makeshift bandage, dripping onto the floor.\n"
                        "The car. If you can get back to the car, find that fuse, get it running...\n"
                        "A hospital. Antibiotics. Stitches.\n"
                        "But that means going back outside. Back where that thing is.\n"
                        "And right now, you can barely stand.\n"
                        "You need to stop the bleeding first. Find something in this house.\n"
                        "Anything.\n"
                        "Before you lose too much blood to make it back.\n"
                    )
            elif decision_6.lower() == 'run':
                typewriter_print(
                    "----------------------------------\n"
                    "No. This is wrong. All of it.\n"
                    "You turn and run back toward the house.\n"
                    "Behind you, something crashes through the undergrowth.\n"
                    "Fast. Getting closer.\n"
                    "You don't look back.\n"
                    "You hit the porch and throw yourself through the door, slamming it shut.\n"
                    "Something heavy slams against it from the outside.\n"
                    "Then another hit. And another.\n"
                    "You hear sniffing along the bottom of the door.\n"
                    "Heavy breathing. A low growl.\n"
                    "Then... silence.\n"
                    "You stand there, trembling, waiting.\n"
                    "Whatever it was, it's gone.\n"
                    "For now.\n"
                )
            else:
                invalid_choice()
        elif decision_5.lower() == 'back':
            typewriter_print(
                "----------------------------------\n"
                "This doesn't feel right. Those sounds...\n"
                "You turn back toward the house and walk quickly up the hill.\n"
                "Behind you, the sounds stop abruptly.\n"
                "You can feel something watching you. Tracking your movement.\n"
                "You don't run. Running triggers chase.\n"
                "But you walk fast. Very fast.\n"
                "When you reach the house, you slip inside and lock the door.\n"
                "Safe.\n"
                "But you can't shake the feeling that something is out there.\n"
                "Waiting.\n"
            )
        else:
            invalid_choice()
    elif decision_4.lower() == 'house':
        typewriter_print(
            "----------------------------------\n"
            "The sounds unsettle you, but the house is right there.\n"
            "Warm light in the windows. Shelter.\n"
            "You turn away from the woods and hurry up the hill.\n"
            "The feeling of being watched follows you all the way to the door.\n"
            "When you reach it, you find it slightly ajar.\n"
            "You push it open and step inside quickly, locking it behind you.\n"
            "If something was out there, at least you're safe now.\n"
            "At least, you hope you are.\n"
        )
    else:
        invalid_choice()

    typewriter_print(
        "----------------------------------\n"
        "As your eyes adjust to the dim light, you find yourself in a small living room.\n"
        "A fireplace crackles softly in the corner, casting dancing shadows across the walls.\n"
        "The room is cozy, almost too cozy — like someone was just here moments ago.\n"
        "A cup of tea sits on the side table, still steaming.\n"
        "But there's no one here.\n"
    )

    # Branching consequences of injured_by_wolf
    if injured_by_wolf:
        typewriter_print(
            "----------------------------------\n"
            "You try to take a step forward, but your leg buckles.\n"
            "The pain explodes through you, sharp and blinding.\n"
            "You grab the doorframe to steady yourself, leaving a bloody handprint.\n"
            "When you look down, your makeshift bandage is completely soaked through.\n"
            "Dark red pools on the hardwood floor.\n"
            "Your vision swims. The room tilts.\n"
            "You need to find something — now — or you're going to pass out.\n"
            "Through the haze, you make out two options:\n"
            "A tall bookshelf against the far wall, packed with old volumes.\n"
            "And a TV cabinet near the fireplace, drawers slightly ajar.\n"
            "\nWhich do you search first — the bookshelf or the TV cabinet? (Type 'BOOKSHELF' or 'CABINET') "
        )
        decision_8 = input("")
        if decision_8.lower() == 'bookshelf':
            typewriter_print(
                "----------------------------------\n"
                "You limp to the bookshelf, using furniture for support.\n"
                "Each step leaves a red smear on the floor.\n"
                "The shelves are crammed with books — old, leather-bound, spine text faded.\n"
                "You run your fingers across them desperately, looking for anything medical.\n"
                "'Folk Remedies of the Northern Tribes'\n"
                "'Medicinal Herbs and Their Applications'\n"
                "'The Lunar Cycle and Its Effects'\n"
                "None of these will help you now.\n"
                "Then, on the middle shelf, two items catch your eye.\n"
                "A thick book, its cover decorated with a carved wolf's head. The title reads: 'Lycanthropy: Curse and Cure'\n"
                "And beside it, a leather journal, worn and stained, held shut with a leather cord.\n"
                "Your vision blurs again. You steady yourself against the shelf.\n"
                "You can only grab one before you collapse.\n"
                "\nDo you take the journal or the book about lycanthropy? (Type 'JOURNAL' or 'BOOK') "
            )
            decision_9 = input("")
            if decision_9.lower() == 'journal':
                if amulet_found:
                    typewriter_print(
                        "----------------------------------\n"
                        "You grab the journal and stumble back toward the fireplace.\n"
                        "Your fingers fumble with the leather cord, finally pulling it loose.\n"
                        "The pages fall open.\n"
                        "But there are no words. No letters.\n"
                        "Just... symbols. Strange, angular markings scratched into the yellowed paper.\n"
                        "They shouldn't make sense.\n"
                        "But they do.\n"
                        "The moment your eyes focus on them, understanding floods your mind.\n"
                        "You reach into your pocket, touching the carved tooth you found.\n"
                        "It's warm. Almost hot.\n"
                        "The symbols in the journal pulse with the same warmth.\n"
                        "They're connected.\n"
                        "But you can't focus on this now. The bleeding—\n"
                        "Your vision darkens at the edges.\n"
                        "You look around desperately and spot the fireplace.\n"
                        "Hot coals glow orange in the grate. A fire poker rests beside it.\n"
                        "You know what you have to do.\n"
                        "Cauterization. Brutal. Primitive. But it will stop the bleeding.\n"
                        "You shove the journal into your pocket with the tooth.\n"
                        "Your hand shakes as you grab the poker and lift a glowing coal.\n"
                        "**This is going to hurt.**\n"
                        "You press it against the wound.\n"
                        "The pain is—\n"
                        "White.\n"
                        "Searing.\n"
                        "Absolute.\n"
                        "You hear yourself screaming, but it sounds distant, like someone else.\n"
                        "The smell of burning flesh fills your nostrils.\n"
                        "The room spins.\n"
                        "Then nothing.\n"
                        "\n"
                        "...\n"
                        "\n"
                        "You wake to darkness.\n"
                        "How long were you out? Minutes? Hours?\n"
                        "Your leg throbs with a dull, deep ache, but the sharp agony is gone.\n"
                        "You touch the wound carefully — the bleeding has stopped.\n"
                        "Seared flesh. Crude. But effective.\n"
                        "The journal is still in your pocket. The tooth too.\n"
                        "Both warm against your skin.\n"
                        "As you pull yourself up, you hear something from the kitchen.\n"
                        "Movement. Deliberate.\n"
                        "You're not alone in this house.\n"
                    )
                    leg_was_treated = True
                    coal_used = True
                else:
                    typewriter_print(
                        "----------------------------------\n"
                        "You grab the journal and try to open it, but the symbols on the first page...\n"
                        "They're meaningless. Alien. They swim before your eyes like insects.\n"
                        "You try to focus, but the pain in your leg spikes.\n"
                        "Your vision tunnels.\n"
                        "The journal slips from your hands.\n"
                        "You reach for the shelf to steady yourself, but your fingers find only air.\n"
                        "The floor rushes up to meet you.\n"
                        "\n"
                        "...\n"
                        "\n"
                        "You wake slowly, consciousness returning in pieces.\n"
                        "You're lying on the floor beside the bookshelf.\n"
                        "A pool of blood has spread beneath your leg.\n"
                        "Too much blood.\n"
                        "Your head pounds. Your mouth is dry.\n"
                        "How long were you out?\n"
                        "The wound hasn't been treated. The bleeding has slowed, but only because you have less blood to lose.\n"
                        "You feel weak. Hollow.\n"
                        "As you struggle to sit up, you hear a sound from the kitchen.\n"
                        "Something moving. Sniffing.\n"
                        "It got inside.\n"
                    )
            elif decision_9.lower() == 'book':
                typewriter_print(
                    "----------------------------------\n"
                    "You grab the heavy book and collapse into a nearby chair.\n"
                    "Your hands shake as you flip through the pages.\n"
                    "'Lycanthropy: A Historical Account'\n"
                    "'Symptoms and Transformation Cycles'\n"
                    "'Methods of Containment'\n"
                    "None of this helps you now—\n"
                    "Wait.\n"
                    "A loose page falls from the center of the book.\n"
                    "Hand-written. Different from the printed text.\n"
                    "'Emergency Treatment for Lycanthropic Wounds'\n"
                    "A recipe. Ingredients listed in careful script.\n"
                    "Your heart pounds. This is exactly what you need.\n"
                    "But the ingredients — where would you even—\n"
                    "Something falls from between the pages.\n"
                    "A small cloth bundle, tied with twine.\n"
                    "You unwrap it with trembling fingers.\n"
                    "**Every ingredient from the recipe. Dried. Preserved. Ready.**\n"
                    "Someone left this here.\n"
                    "Someone knew.\n"
                    "You don't have time to question it.\n"
                    "Using a mortar and pestle from the mantle, you grind the herbs according to the instructions.\n"
                    "The mixture turns into a thick, dark paste that smells of pine and something else. Something earthy and old.\n"
                    "You tear away your blood-soaked bandage and apply the salve directly to the wound.\n"
                    "It burns at first — a different burn than fire, colder somehow.\n"
                    "Then... relief.\n"
                    "Not complete. The wound still aches. Still throbs.\n"
                    "But the bleeding stops. The pain dulls to something manageable.\n"
                    "You can feel the salve working, pulling the torn flesh together.\n"
                    "You lean back, exhausted, and notice a notation at the bottom of the recipe:\n"
                    "'This will halt the transformation, but not reverse it. The curse remains dormant. Use with caution.'\n"
                    "Transformation?\n"
                    "Curse?\n"
                    "What does that—\n"
                    "A noise from the kitchen interrupts your thoughts.\n"
                    "Something's in there.\n"
                )
                leg_was_treated = True
                salve_used = True
            else:
                invalid_choice()
        elif decision_8.lower() == 'cabinet':
            typewriter_print(
                "----------------------------------\n"
                "You lurch toward the TV cabinet, gripping the furniture as you go.\n"
                "Your leg drags behind you, leaving a crimson trail.\n"
                "You yank open the first drawer.\n"
                "Old magazines. TV guides from years ago. A remote with dead batteries.\n"
                "Nothing useful.\n"
                "Your breathing is ragged. The room feels too hot.\n"
                "From somewhere else in the house — the kitchen, maybe — you hear a sound.\n"
                "Faint. Could be the wind rattling a door.\n"
                "Or a door being opened.\n"
                "\nDo you want to keep searching the cabinet or investigate the kitchen? (Type 'SEARCH' or 'KITCHEN') "
            )
            decision_10 = input("")
            if decision_10.lower() == 'search':
                typewriter_print(
                    "----------------------------------\n"
                    "You wrench open the second drawer, sending magazines scattering across the floor.\n"
                    "And there — wedged in the back — a white plastic box with a red cross.\n"
                    "'First aid kit'.\n"
                    "Your hands shake as you pull it out and snap it open.\n"
                    "Gauze. Antiseptic. Medical tape. Actual supplies.\n"
                    "You work quickly, tearing open packets with your teeth.\n"
                    "The antiseptic burns as you pour it over the wound, and you bite back a scream.\n"
                    "You pack the punctures with gauze, wrapping them tightly with medical tape.\n"
                    "It's not pretty. It's not professional.\n"
                    "But the bleeding slows. Then stops.\n"
                    "You lean back against the cabinet, breathing hard.\n"
                    "The pain is still there — deep, throbbing — but manageable.\n"
                    "This won't heal on its own, though. Those punctures are deep.\n"
                    "You need a hospital. Antibiotics. Proper stitches.\n"
                    "Infection is going to be a problem if you don't get real medical help soon.\n"
                    "But for now, you're stable.\n"
                    "As you catch your breath, the sound from the kitchen comes again.\n"
                    "Closer this time.\n"
                    "Deliberate.\n"
                )
                leg_was_treated = True
                first_aid_used = True
            elif decision_10.lower() == 'kitchen':
                typewriter_print(
                    "----------------------------------\n"
                    "The sound comes again — louder.\n"
                    "Definitely from the kitchen.\n"
                    "You abandon the search and push yourself upright.\n"
                    "Big mistake.\n"
                    "The moment you put weight on your injured leg, the pain detonates.\n"
                    "Your vision goes white. Your knees buckle.\n"
                    "You collapse onto the sofa, gasping, clutching your leg.\n"
                    "The wound has opened wider. Blood flows freely again.\n"
                    "Your head swims. The ceiling spins above you.\n"
                    "You try to focus, but consciousness keeps slipping away.\n"
                    "Somewhere in the distance, you hear the kitchen sound again.\n"
                    "Closer.\n"
                    "You need to get up. Need to move.\n"
                    "But your body won't respond.\n"
                    "\n"
                    "...\n"
                    "\n"
                    "When you open your eyes, you don't know how much time has passed.\n"
                    "Seconds? Minutes?\n"
                    "The bleeding has slowed, but only because there's less blood left to lose.\n"
                    "Your lips are dry. Your skin is cold.\n"
                    "Shock, probably.\n"
                    "The wound is still open. Still dangerous.\n"
                    "And the sound from the kitchen has stopped.\n"
                    "That should make you feel better.\n"
                    "It doesn't.\n"
                )
            else:
                invalid_choice()
        else:
            invalid_choice()
    else:
        typewriter_print(
            "----------------------------------\n"
            "The house is quiet except for the crackling fire.\n"
            "And something else.\n"
            "A sound from deeper in the house.\n"
            "The kitchen, you think.\n"
            "Could be the wind. An open window.\n"
            "Could be the owner of this house, finally showing themselves.\n"
            "Or it could be something else entirely.\n"
            "\nYou move cautiously toward the kitchen, staying alert.\n"
        )

    # Branch consequences of car_was_destroyed
    if not car_was_destroyed:
        if leg_was_treated:
            typewriter_print(
                "----------------------------------\n"
                "You steady yourself and look around the living room.\n"
                "The kitchen sounds continue — wet, rhythmic, accompanied by low breathing.\n"
                "It's feeding.\n"
                "Whatever's in there is too focused on its meal to notice you.\n"
                "For now.\n"
                "The smell reaches you — raw meat, blood, the sharp tang of a fresh kill.\n"
                "Near the window, you spot a small desk, its drawer hanging open.\n"
                "Cables spill from it. Papers scattered inside.\n"
                "If there's a replacement fuse in this house, it would be there.\n"
                "That fuse could get your car running. Get you out of here.\n"
                "But every movement risks noise.\n"
                "And the thing in the kitchen... you don't know how long it'll stay distracted.\n"
            )
        else:
            typewriter_print(
                "----------------------------------\n"
                "You're still on the floor, or slumped against furniture.\n"
                "The room tilts and sways.\n"
                "Too much blood lost. Too much time passed.\n"
                "From the kitchen, the sounds continue.\n"
                "Wet tearing. Heavy chewing. Something being consumed.\n"
                "The smell hits you — raw meat, blood.\n"
                "It's in there. Feeding.\n"
                "You need to move. Need to hide. Need to do *something*.\n"
                "But your body barely responds.\n"
                "Near the window, there's a desk. Drawer open.\n"
                "Maybe there's something useful there.\n"
                "Or maybe you should just stay still. Silent.\n"
                "Hope it finishes and leaves.\n"
                "Every choice could be your last.\n"
            )    
        typewriter_print(
            "\nDo you search the desk for supplies or check what's in the kitchen? (Type 'DESK' or 'KITCHEN') "
        )
        decision_11 = input("")
        if decision_11.lower() == 'desk':
            typewriter_print("----------------------------------")
            if not leg_was_treated:
                typewriter_print(
                    "You drag yourself toward the desk.\n"
                    "Each movement is agony. Your leg leaves a blood trail across the floor.\n"
                    "Smear. Drag. Smear.\n"
                    "The desk is only ten feet away.\n"
                    "It might as well be a mile.\n"
                    "You grip the edge and pull yourself up, gasping.\n"
                    "Black spots dance in your vision.\n"
                    "The drawer hangs open. Cables. Papers. Junk.\n"
                    "Your hands shake as you search.\n"
                    "From the kitchen: a loud **CRACK**.\n"
                    "Bone breaking. Marrow being consumed.\n"
                    "You freeze, hand buried in the drawer.\n"
                    "The chewing continues.\n"
                    "It hasn't noticed you.\n"
                    "Yet.\n"
                    "You keep searching, moving as quietly as your trembling hands allow.\n"
                )
            else:
                typewriter_print(
                    "You move to the desk, keeping your steps light.\n"
                    "Your treated leg aches with each step, but you can manage.\n"
                    "The drawer is already open, spilling cables and papers.\n"
                    "You start searching carefully, trying not to make noise.\n"
                    "Old receipts. Instruction manuals. Dead batteries.\n"
                    "From the kitchen, the sounds continue.\n"
                    "Wet tearing. Bone cracking. Heavy breathing.\n"
                    "Whatever it's eating is substantial.\n"
                    "Keeping it occupied.\n"
                    "A loud SNAP makes you flinch — another bone breaking.\n"
                    "But the chewing doesn't stop.\n"
                    "It's too focused on its meal to notice you.\n"
                    "You keep searching.\n"
                )
            typewriter_print(
                "\nA crash from the kitchen — something metal hitting the floor. Do you keep searching or investigate? (Type 'SEARCH' or 'KITCHEN') "
            )
            decision_12 = input("")
            if decision_12.lower() == 'search':
                typewriter_print("----------------------------------")
                if not leg_was_treated:
                    typewriter_print(
                        "You decide to keep searching despite the pain.\n"
                        "Your vision tunnels. The edges go gray.\n"
                        "Blood loss. You're running out of time.\n"
                        "You push deeper into the drawer, ignoring the cables that snag your fingers.\n"
                        "A loud crash from the kitchen — something heavy hitting the floor.\n"
                        "Then a wet dragging sound.\n"
                        "**It's moving.**\n"
                        "Your heart hammers. Your hands won't stop shaking.\n"
                        "Papers scatter. Cables fall.\n"
                        "From the kitchen: a low, rumbling growl.\n"
                        "Not the satisfied sound of eating.\n"
                        "You knocked something over. It heard.\n"
                        "The dragging sound stops.\n"
                        "Silence.\n"
                        "Then: sniffing.\n"
                        "Getting closer.\n"
                        "**It's coming.**\n"
                    )
                    return
                else:
                    typewriter_print(
                        "You dig deeper, moving cables aside methodically.\n"
                        "Papers. More cables. Old phone chargers.\n"
                        "Your fingers brush something small and cylindrical at the bottom.\n"
                        "**Wait—**\n"
                        "From the kitchen: a loud crash.\n"
                        "Metal clattering. Something heavy knocked over.\n"
                        "The chewing stops abruptly.\n"
                        "You freeze.\n"
                        "A low growl rumbles through the house.\n"
                        "Then claws on linoleum. **Click. Click. Click.**\n"
                        "Coming this way.\n"
                        "It's no longer distracted.\n"
                    )
                
                typewriter_print(
                    "\nThe growling is getting closer. Do you keep searching desperately or face what's coming? (Type 'SEARCH' or 'KITCHEN') "
                )
                decision_13 = input("Do you want to keep searching the desk or finally go to the kitchen? (Type 'SEARCH' or 'KITCHEN') ")
                if decision_13.lower() == 'search':
                    typewriter_print("----------------------------------")
                    if not leg_was_treated:
                        typewriter_print(
                            "You can't stop now. You're so close.\n"
                            "Your hands tear through the drawer, frantic.\n"
                            "Papers fly. Cables snap.\n"
                            "**There!**\n"
                            "At the very bottom, wedged in the back corner.\n"
                            "A car fuse. The right size.\n"
                            "You grab it, shoving it into your pocket.\n"
                            "But the movement costs you.\n"
                            "Your leg gives out. You collapse against the desk.\n"
                            "The desk scrapes loudly across the floor.\n"
                            "**No no no—**\n"
                            "The growling from the kitchen becomes a snarl.\n"
                            "You hear it burst through the doorway.\n"
                            "Claws scrabbling. Paws hitting hardwood.\n"
                            "You turn your head.\n"
                            "It's right there.\n"
                            "Massive. Dark fur matted with blood. Eyes glowing in the firelight.\n"
                            "Its muzzle is stained red, lips pulled back over teeth as long as your fingers.\n"
                            "This is the same creature that bit you.\n"
                            "And now you're on the ground, bleeding, helpless.\n"
                            "It recognizes you too. Its snarl deepens.\n"
                            "Prey that got away.\n"
                            "It lunges.\n"
                            "You try to crawl, but your leg is useless.\n"
                            "Its jaws close around your throat.\n"
                            "The pressure is immense. Crushing.\n"
                            "You can't scream. Can't breathe.\n"
                            "The last thing you feel is your blood, hot against your skin.\n"
                            "The last thing you see is those yellow eyes, burning with hunger.\n"
                            "GAME OVER\n"
                        )
                        return
                    else:
                        typewriter_print(
                            "You have to find it. Now.\n"
                            "Your hands dive to the bottom of the drawer.\n"
                            "And there — wedged in the corner — a car fuse.\n"
                            "**Yes!**\n"
                            "You grab it and shove it into your pocket.\n"
                            "The clawing sounds are right outside the living room.\n"
                            "You turn toward the kitchen doorway.\n"
                            "**It's there.**\n"
                            "Massive. Dark. Blood dripping from its muzzle.\n"
                            "The wolf from the forest.\n"
                            "It found you.\n"
                            "Its eyes lock onto yours.\n"
                            "Yellow. Glowing. Intelligent.\n"
                            "It remembers you.\n"
                            "Its lips pull back in a snarl.\n"
                            "But then it hesitates.\n"
                            "Your leg. The bandage. The smell of the treatment.\n"
                            "Something about you has changed.\n"
                            "It tilts its head, nostrils flaring.\n"
                            "Confusion. Almost... recognition?\n"
                            "The moment stretches.\n"
                            "Then a low growl builds in its chest.\n"
                            "Hunger wins.\n"
                            "You have the fuse. But the wolf is between you and the door.\n"
                            "The back door — through the kitchen — that's your only escape route.\n"
                            "You need to move. Now.\n"
                        )
                        fuse_found = True
                elif decision_13.lower() == 'kitchen':
                    typewriter_print("----------------------------------")
                    if not leg_was_treated:
                        typewriter_print(
                            "You abandon the search and turn toward the kitchen.\n"
                            "Each step sends lightning through your leg.\n"
                            "You grip the wall, the furniture, anything to stay upright.\n"
                            "Blood trails behind you.\n"
                            "As you reach the kitchen doorway, you see it.\n"
                            "**The wolf.**\n"
                            "Massive. Shoulders as high as your waist.\n"
                            "It's standing over something on the floor — dark, torn, unrecognizable.\n"
                            "Its muzzle is stained red, dripping.\n"
                            "When it sees you, it goes still.\n"
                            "Those yellow eyes lock onto yours.\n"
                            "**Recognition.**\n"
                            "This is the creature that bit you.\n"
                            "Its lips pull back slowly. A warning growl.\n"
                            "You try to back away, but your leg gives out.\n"
                            "You collapse, hitting the floor hard.\n"
                            "The wolf's ears prick forward.\n"
                            "**Weakness.**\n"
                            "It smells your blood. Fresh. Flowing.\n"
                            "The growl becomes a snarl.\n"
                            "It charges.\n"
                            "You raise your arms instinctively, but it's pointless.\n"
                            "The weight of it crashes into you.\n"
                            "Teeth find your throat.\n"
                            "The pain is sharp, then numb, then nothing.\n"
                            "GAME OVER\n"
                        )
                        return
                    else:
                        typewriter_print(
                            "You steel yourself and move toward the kitchen.\n"
                            "Your leg protests, but you can manage.\n"
                            "At the doorway, you stop.\n"
                            "**There it is.**\n"
                            "The wolf. The same one from the forest.\n"
                            "It's hunched over something on the floor.\n"
                            "Dark. Bloody. You don't look too closely.\n"
                            "The creature is enormous in the enclosed space.\n"
                            "Its fur is matted with blood and dirt.\n"
                            "As you watch, it tears another chunk of meat free.\n"
                            "Then it pauses.\n"
                            "Its head lifts slowly.\n"
                            "Nostrils flare.\n"
                            "It smells you.\n"
                            "Those yellow eyes turn toward you.\n"
                            "For a moment, neither of you moves.\n"
                            "Your treated wound throbs. The salve. The medicine.\n"
                            "The wolf's nostrils flare again.\n"
                            "Its head tilts, almost curious.\n"
                            "Something about your scent has changed.\n"
                            "But then its lips pull back.\n"
                            "A low growl builds in its chest.\n"
                            "Changed or not, you're still prey.\n"
                            "And it hasn't finished eating.\n"
                            "Behind it, you see the back door — standing open.\n"
                            "That's how it got in.\n"
                            "That's your way out.\n"
                            "But the wolf is between you and freedom.\n"
                        )
                else:
                    invalid_choice()
            elif decision_12.lower() == 'kitchen':
                typewriter_print("----------------------------------")
                if not leg_was_treated:
                    typewriter_print(
                        "You need to know what's in there.\n"
                        "You push away from the desk, using the wall for support.\n"
                        "Each step is agony. Your leg drags uselessly.\n"
                        "Blood soaks through your bandage, dripping with each movement.\n"
                        "You reach the kitchen doorway and peer inside.\n"
                        "**The wolf.**\n"
                        "It's there, hunched over something dark and torn on the floor.\n"
                        "Feeding.\n"
                        "Its shoulders ripple with each movement.\n"
                        "Then it stops.\n"
                        "Its head lifts.\n"
                        "Sniffing.\n"
                        "Your blood.\n"
                        "The wolf turns its head slowly, fixing you with those yellow eyes.\n"
                        "It recognizes you. The prey that escaped.\n"
                        "A low growl rumbles from deep in its chest.\n"
                        "You try to back away, but your leg gives out.\n"
                        "You hit the floor hard.\n"
                        "The wolf is on you before you can even scream.\n"
                        "Its weight crushes you. Its teeth find your neck.\n"
                        "This time, there's no escape.\n"
                        "GAME OVER\n"
                    )
                    return
                else:
                    typewriter_print(
                        "You move toward the kitchen, each step deliberate.\n"
                        "Your leg aches but holds.\n"
                        "At the doorway, you stop and look inside.\n"
                        "**There.**\n"
                        "The wolf. Massive and dark, hunched over its kill.\n"
                        "You can see the back door standing open behind it.\n"
                        "That's how it got in.\n"
                        "The creature tears at the meat, too focused to notice you yet.\n"
                        "But then the wind shifts.\n"
                        "Its ears swivel toward you.\n"
                        "Its head rises slowly.\n"
                        "Nostrils flare. Testing the air.\n"
                        "**It knows you're there.**\n"
                        "Those yellow eyes turn toward you, locking on.\n"
                        "For a heartbeat, neither of you moves.\n"
                        "Then its lips pull back, revealing blood-stained teeth.\n"
                        "A growl builds in its chest.\n"
                        "The back door is right there.\n"
                        "But so is the wolf.\n"
                    )
            else:
                invalid_choice()
        elif decision_11.lower() == 'kitchen':
            typewriter_print("----------------------------------")
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
        if leg_was_treated:
            typewriter_print(
                "----------------------------------\n"
                "You pull yourself to your feet, testing your treated leg.\n"
                "It holds. Painful, but functional.\n"
                "From the kitchen, the sounds continue.\n"
                "Wet tearing. Bone cracking. Heavy, rhythmic breathing.\n"
                "Feeding.\n"
                "The smell drifts through the house — raw meat, blood, animal musk.\n"
                "Whatever's in there is consuming something.\n"
                "The car is gone. Burned. No escape that way.\n"
                "You're trapped in this house with it.\n"
                "The front door is locked — you made sure it was when you came in.\n"
                "Which means the only other exit is through the kitchen.\n"
                "The back door.\n"
                "But that means getting past whatever's in there.\n"
                "You need to know what you're dealing with.\n"
                "You need to see it.\n"
            )
        else:
            # Untreated wound + no car = death is imminent
            typewriter_print(
                "----------------------------------\n"
                "You try to move, but your wounded leg gives out instantly.\n"
                "A sharp, burning pain cuts through you like a blade.\n"
                "You let out a strained cry before you can stop yourself.\n"
                "It's enough.\n"
                "The sounds from the kitchen stop abruptly.\n"
                "Silence.\n"
                "Then you hear it — claws on linoleum.\n"
                "Click. Click. Click.\n"
                "Coming closer.\n"
                "Through the kitchen doorway, you see movement.\n"
                "A massive shape. Dark fur. Eyes reflecting the firelight.\n"
                "The wolf.\n"
                "Its muzzle is stained red. Dripping.\n"
                "It sees you on the floor. Wounded. Bleeding. Helpless.\n"
                "Its lips pull back in a snarl.\n"
                "Prey.\n"
                "You try to crawl, but there's nowhere to go.\n"
                "The wolf crosses the distance in two bounds.\n"
                "Its weight crushes you to the floor.\n"
                "Teeth sink into your throat.\n"
                "The pressure is immense. Final.\n"
                "You should have treated your wound.\n"
                "You should have stayed quiet.\n"
                "GAME OVER\n"
            )
            return
        typewriter_print(
            "\nYou move cautiously toward the kitchen, staying alert.\n"
        )

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