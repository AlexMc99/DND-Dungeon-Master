import TextScanner

response = TextScanner.main()

def roomCheck(roomNumber):
    with open("savedata.txt", "r") as file:
        lines = file.readlines()
        if lines[roomNumber - 1] == "0":
            return True
        else:
            return False

def roomWrite(roomNumber):
    newLine = "1"
    with open("savedata.txt", "r") as file:
        lines = file.readlines()
        lines[roomNumber - 1] = newLine
    with open("savedata.txt", "w") as file:
        file.writelines(lines)
    file.close()

def sneakChecker(npcValue):
    rolled = roll()
    if (user.intelligence + rolled) > (npcValue * 2):
        return True
    else:
        return False

def attackChecker(npcValue):
    rolled = roll()
    if (user.strength + rolled) > npcValue:
        return True
    else:
        return False

def attackSequence(npcValue):
    if attackChecker(npcValue):
        print("The attack was successful!")
        return True

    else:
        print("The attack was not successful!")
        user.health = user.health - npcValue
        return False

def introduction():
    print('''
    It has been a long journey, bit it will pay off soon. Do you rember what
    happened?
    ...

    Your brother was kidnapped by the King of Trolls duringan invasion on your
    homeland, the Kingdom of Glott. Cattle was killed, homes were burned, and
    innocent lives were lost in the slaughter. Your brother, King Consort
    Hannibal, married to Queen Regnant Demetria, was kidnapped during the
    invasion.

    You have been venturing through the marshy, barbaric Land of Boog in hopes
    of finding yourbrother. It has been exhausting. You’ve been ambushed,
    beaten, and gone so far as nearly losing your own life. But it has all been
    worth it. It has all led you to an abandoned prison, deep within the woods.
    It may all have been a rumor, maybe even a trap, but you are desperate for
    answers. You want your brother back. Your life back.

    You enter the abandoned building.
    ''')

def room3():
    if roomCheck(3):
        roomWrite(3)
        print('''
        Upon entering, you see a torch to your left. Do you wish to take it?
        ''')

        if response == "Yes":
            print('''
            You decided to take the torch.

            It will help to illumiate the pathway for you.

            You go through the door, not knowing what awaits you on the other side.
            ''')

        else:
            print('''
            You decided not to take the torch.

            Your endeavor will be harder with your limited field of sight.

            You go through the door, not knowing what awaits you on the other side.
            ''')

    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if userinput == "north":
                print("Heading to room 4 . . .")
                room4()
                rooms = 0
            else:
                print("You cannot enter this area. Try again.")
def room4():
    if roomCheck(4):
        roomWrite(4)
        print('''
        You hear a creaking noise down the hallway, what do you do?
        ''')
        npcStrength = 10
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            You chose to quietly venture down the hall, peeking around the corner as you
            approach. Ahead of you are two men, both heavily armed. You will need to subdue both
            at the same time to be successful. Jareth and Hogarth are two trolls with an attitude problem.
            Can you do it?
            ''')

            if sneakChecker(npcStrength) == False:
                print("You did not succeed in taking down Jareth and Hogarth. You must now be forced to battle. Good luck")

                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received 1 health potion. What now?")
                            bodyCheck = 1
                            user.health = user.health + 15
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. Sadly, there is nothing of value inside. Better luck next time!")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")

                    if direction == north:
                        print("Heading to room 2 . . .")
                        room2()
                    else:
                        print("You cannot enter this area. Try again.")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received 1 health potion. What now?")
                            bodyCheck = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. Sadly, there is nothing of value inside. Better luck next time!")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")
                    print("What direction would you like to go?")

                    if direction == north:
                        print("Heading to room 2 . . .")
                        room2()
                    else:
                        print("You cannot enter this area. Try again.")
            else:
                print("You succeeded in stealthily taking them down. Now what?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received 1 health potion. What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. Sadly, there is nothing of value inside. Better luck next time!")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                    print("What direction would you like to go?")

                    if direction == north:
                        print("Heading to room 2 . . .")
                        room2()
                    else:
                        print("You cannot enter this area. Try again.")


        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")

                while room == 4:
                    ###get input
                    if userinput == "body":
                        print("You decided to check their bodies and received 1 health potion. What now?")
                    elif userinput == "room":
                        print("You decided to check the room. Sadly, there is nothing of value inside. Better luck next time!")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")

                rooms = 1
                while rooms != 0:
                    if direction == "north":
                        print("Heading to room 2 . . .")
                        room2()
                        rooms = 0
                    else:
                        print("You cannot enter this area. Try again.")



            else:
                print("You must roll again.")
                while attackSequence(npcStrength) == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body":
                        print("You decided to check their bodies and received 1 health potion. What now?")
                    elif userinput == "room":
                        print("You decided to check the room. Sadly, there is nothing of value inside. Better luck next time!")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                    print("What direction would you like to go?")

                rooms = 1
                while rooms != 0:
                    if direction == "north":
                        print("Heading to room 2 . . .")
                        room2()
                        rooms = 0
                    else:
                        print("You cannot enter this area. Try again.")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == "north":
                print("Heading to room 2 . . .")
                room2()
                rooms = 0
            else:
                print("You cannot enter this area. Try again.")

def room2():
    if roomCheck(2):
        roomWrite(2)
        print('''
        You hear two voices and the conversation immediately cuts short upon your
        entry. You look up and see a large toad and a miniscule troll standing at a
        table in the center of the room, their eyes quickly dart to you. You can see
        fear flicker across their faces.

        "Wh-who are you?!” the Toad demands, voice quivering.

        What do you do?
        ''')
        npcStrength = 25
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            You are unable to sneak. They've already spotted you. But, maybe if you're lucky and charismatic enough,
            they will think you're one of them!
            ''')
            if sneakChecker(npcStrength) == False:
                print("You did not succeed in blending in. You must now be forced to battle. Good luck")
                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received a rusty sword, a rickety helmet, a health potion, and a piece of cloth. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 3
                            user.health = user.health + 15
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find some matches.")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading to room 1 . . .")
                            room1()
                            rooms = 0
                        elif direction == south:
                            print("Heading to room 4 . . .")
                            room4()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 7 . . .")
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received a rusty sword, a rickety helmet, a health potion, and a piece of cloth. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 3
                            user.health = user.health + 15
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find some matches.")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")
                    print("What direction would you like to go?")

                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading to room 1 . . .")
                            room1()
                            rooms = 0
                        elif direction == south:
                            print("Heading to room 4 . . .")
                            room4()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 7 . . .")
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")
            else:
                print("You succeeded in stealthily taking them down. Now what?")
                while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received a rusty sword, a rickety helmet, a health potion, and a piece of cloth. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 3
                            user.health = user.health + 15
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find some matches.")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                print("What direction would you like to go?")

                rooms = 1
                while rooms != 0:
                        if direction == north:
                            print("Heading to room 1 . . .")
                            room1()
                            rooms = 0
                        elif direction == south:
                            print("Heading to room 4 . . .")
                            room4()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 7 . . .")
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a rusty sword, a rickety helmet, a health potion, and a piece of cloth. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 3
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find some matches.")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")

                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 1 . . .")
                        room1()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 4 . . .")
                        room4()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 7 . . .")
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a rusty sword, a rickety helmet, a health potion, and a piece of cloth. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 3
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find some matches.")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 1 . . .")
                        room1()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 4 . . .")
                        room4()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 7 . . .")
                        room7()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == north:
                print("Heading to room 1 . . .")
                room1()
                rooms = 0
            elif direction == south:
                print("Heading to room 4 . . .")
                room4()
                rooms = 0
            elif direction == east:
                print("Heading to room 7 . . .")
                room7()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")

def room3():
    if roomCheck(1):
        roomWrite(1)
        print('''
        This room is a dead end. You look around and notice a puddle of goo on the
        floor next to a shackled skeleton. What do you do? Would you like to explore the room
        or move on?
        ''')

        if response == "Yes":
            print('''
            You decided to check out the goo...

            You chose to approach it. In your overwhelming curiosity, you managed to inhale a
            strange vapor surrounding the ooze. Your intelligence has gone down 2 points and
            your HP has gone down 15 points. The vapor has put you in a daze and made you feel
            sickly. You decide to quickly leave the room and try to get some fresh air.

            ''')
            user.intelligence = user.intelligence - 2
            user.health = user.health - 15
            room2()

        else:
            print('''
            You decided not to approach the toxic goo. That was a good idea.

            It's time to head back to room 2.

            ''')
            room2()



    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if userinput == "south":
                print("Heading to room 2 . . .")
                room2()
                rooms = 0
            else:
                print("You cannot enter this area. Try again.")

def room7():
    if roomCheck(7):
        roomWrite(7)
        print('''
        There’s no time to react! You’re being ambushed! Quickly, what do you do?
        The evil Lobster Todd is known through the kingdom for causing terror and
        anguish in your fellow humans with his evil, lobster ways.
        ''')
        npcStrength = 21
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "Wait":
            print('''
            This was not the best option...
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their body and received a health potion. What now?")
                        bodyCheck = 1
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything useful.")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 8 . . .")
                        room8()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 15 . . .")
                        room(15)
                        rooms = 0
                    else:
                        room2()
                        rooms = 0


            else:
                print("You must roll again.")
                while attackSequence(npcStrength) == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their body and received a health potion. What now?")
                        bodyCheck = 1
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything useful.")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 8 . . .")
                        room8()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 15 . . .")
                        room(15)
                        rooms = 0
                    else:
                        room2()
                        rooms = 0

        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")

                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their body and received a health potion. What now?")
                        bodyCheck = 1
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything useful.")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 8 . . .")
                        room8()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 15 . . .")
                        room(15)
                        rooms = 0
                    else:
                        room2()
                        rooms = 0

            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and received a health potion. What now?")
                        bodyCheck = 1
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything useful.")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 8 . . .")
                        room8()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 15 . . .")
                        room(15)
                        rooms = 0
                    else:
                        room2()
                        rooms = 0
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == north:
                print("Heading to room 6 . . .")
                room6()
                rooms = 0
            elif direction == south:
                print("Heading to room 8 . . .")
                room8()
                rooms = 0
            elif direction == east:
                print("Heading to room 15 . . .")
                room(15)
                rooms = 0
            else:
                room2()
                rooms = 0

def room6():
    if roomCheck(6):
        roomWrite(6)
        print('''
        You hear a pacing noise coming from the north. What do you do?
        ''')
        npcStrength = 30
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            Peering down the hallway, you see them. The notorious goblin twins Zoey and Joey.
            You recognize them as two people that were in the group of thieves that kidnapped
            your brother.

            Let's see if they've spotted you.

            ''')
            if sneakChecker(npcStrength) == False:
                print("You did not succeed in sneaking in. They easily spotted you and let out an angry snarl as they charge toward you.")
                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received 5 health potions and a new shield! What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 9
                            user.health = user.health + (15 * 5)
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find a new dagger!")
                            roomChecks = 1
                            user.strength = user.strength + 4
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading to room 5 . . .")
                            room5()
                            rooms = 0
                        elif direction == south:
                            print("Heading to room 7 . . .")
                            room7()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received 5 health potions and a new shield! What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 9
                            user.health = user.health + (15 * 5)
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find a new dagger!")
                            roomChecks = 1
                            user.strength = user.strength + 4
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading to room 5 . . .")
                            room5()
                            rooms = 0
                        elif direction == south:
                            print("Heading to room 7 . . .")
                            room7()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")

            else:
                print("You succeeded in stealthily taking them down. Now what?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received 5 health potions and a new shield! What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 9
                        user.health = user.health + (15 * 5)
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find a new dagger!")
                        roomChecks = 1
                        user.strength = user.strength + 4
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 5 . . .")
                        room5()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 7 . . .")
                        room7()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")



        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received 5 health potions and a new shield! What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 9
                        user.health = user.health + (15 * 5)
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find a new dagger!")
                        roomChecks = 1
                        user.strength = user.strength + 4
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 5 . . .")
                        room5()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 7 . . .")
                        room7()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")


            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received 5 health potions and a new shield! What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 9
                        user.health = user.health + (15 * 5)
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find a new dagger!")
                        roomChecks = 1
                        user.strength = user.strength + 4
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to room 5 . . .")
                        room5()
                        rooms = 0
                    elif direction == south:
                        print("Heading to room 7 . . .")
                        room7()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == north:
                print("Heading to room 5 . . .")
                room5()
                rooms = 0
            elif direction == south:
                print("Heading to room 7 . . .")
                room7()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")

def room5():
    if roomCheck(5):
        roomWrite(5)
        print('''
        You slowly enter the room, a foreboding feeling rippling through your body. On the far side
        of the room is one of the men who attacked you in your castle and helped to kidnap your brother.

        “I see you’ve finally made it to the party, weakling. You’re a little late though. Your brother
        is a bit… Indisposed at the moment. Sorry.” The man in front of you is Michael Scarn. One of the
        great nuisances of the land of Oorg. His band of thieves surrounding him. From left to right is:
        Kevin, Michael, and Toby.


        He takes a step towards you. What will you do?
        ''')
        npcStrength = 45
        room = 4
        bodyCheck = 0
        roomChecks = 0

        if response == "Wait":
            print('''
            This was not the best option...
            ''')
            if attackSequence(npcStrength):
                print('''The final man falls to his knees, holding his middle, blood spurting in every direction.

                “They’ll kill you, just like we did him.”

                Your blood runs cold, fear clouding your senses.

                “My brother is dead?!”

                The man doesn’t respond, a quiet gasp exiting his lungs as his eyes close for the final time.
                With your heart pounding in your chest and your ears ringing, you hunch over, sickness taking over.

                Is your brother dead? Was he lying?

                Now what?
                ''')
                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a gold ring, ancient chestpiece, and a chainmaille scarf. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 21
                    elif userinput == "room" and roomChecks == 0:
                        print("You managed to find 2 health potions!")
                        roomChecks = 1
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == south:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    else:
                        print("Input is invalid! Please try again!")


            else:
                print("You must roll again.")
                while attackSequence(npcStrength) == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print('''The final man falls to his knees, holding his middle, blood spurting in every direction.

                “They’ll kill you, just like we did him.”

                Your blood runs cold, fear clouding your senses.

                “My brother is dead?!”

                The man doesn’t respond, a quiet gasp exiting his lungs as his eyes close for the final time.
                With your heart pounding in your chest and your ears ringing, you hunch over, sickness taking over.

                Is your brother dead? Was he lying?

                Now what?
                ''')

                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a gold ring, ancient chestpiece, and a chainmaille scarf. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 21
                    elif userinput == "room" and roomChecks == 0:
                        print("You managed to find 2 health potions!")
                        roomChecks = 1
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == south:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    else:
                        print("Input is invalid! Please try again!")

        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print('''The final man falls to his knees, holding his middle, blood spurting in every direction.

                “They’ll kill you, just like we did him.”

                Your blood runs cold, fear clouding your senses.

                “My brother is dead?!”

                The man doesn’t respond, a quiet gasp exiting his lungs as his eyes close for the final time.
                With your heart pounding in your chest and your ears ringing, you hunch over, sickness taking over.

                Is your brother dead? Was he lying?

                Now what?
                ''')

                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a gold ring, ancient chestpiece, and a chainmaille scarf. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 21
                    elif userinput == "room" and roomChecks == 0:
                        print("You managed to find 2 health potions!")
                        roomChecks = 1
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == south:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    else:
                        print("Input is invalid! Please try again!")

            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print('''The final man falls to his knees, holding his middle, blood spurting in every direction.

                “They’ll kill you, just like we did him.”

                Your blood runs cold, fear clouding your senses.

                “My brother is dead?!”

                The man doesn’t respond, a quiet gasp exiting his lungs as his eyes close for the final time.
                With your heart pounding in your chest and your ears ringing, you hunch over, sickness taking over.

                Is your brother dead? Was he lying?

                Now what?
                ''')

                while room == 4:
                    ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a gold ring, ancient chestpiece, and a chainmaille scarf. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 21
                    elif userinput == "room" and roomChecks == 0:
                        print("You managed to find 2 health potions!")
                        roomChecks = 1
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == south:
                        print("Heading to room 6 . . .")
                        room6()
                        rooms = 0
                    else:
                        print("Input is invalid! Please try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == south:
                print("Heading to room 6 . . .")
                room6()
                rooms = 0
            else:
                print("Input is invalid! Please try again!")

def room8():

    print('''
    This room is empty. What direction would you like to head in?
    ''')
    rooms = 1
    while rooms != 0:
        if direction == north:
            print("Heading to room 7 . . .")
            room7()
            rooms = 0
        else:
            print("This direction is invalid. Try again!")

def room11():
    if roomCheck(11):
        roomWrite(11)
        print('''
        As you slowly creep into the room, you notice a guard standing just ahead of you.
        What will you do?
        ''')
        npcStrength = 42
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            You read yourself to pounce on him as he is making his rounds.

            Will you succeed?

            ''')
            if sneakChecker(npcStrength) == False:
                print("You did not succeed in sneaking up on him. He easily spotted you and readies for an attack.")
                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body. Sadly, nothing useful was found. What now?")
                            bodyCheck = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find a throwing star!")
                            roomChecks = 1
                            user.strength = user.strength + 2
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading to the cells above . . .")
                            room9and10()
                            rooms = 0
                        elif direction == south:
                            print("Heading to the cells below . . .")
                            room121314()
                            rooms = 0
                        elif direction == east:
                            print("Heading to the hallway . . .")
                            roomHallwayC()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body. Sadly, nothing useful was found. What now?")
                            bodyCheck = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find a throwing star!")
                            roomChecks = 1
                            user.strength = user.strength + 2
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading to the cells above . . .")
                            room9and10()
                            rooms = 0
                        elif direction == south:
                            print("Heading to the cells below . . .")
                            room121314()
                            rooms = 0
                        elif direction == east:
                            print("Heading to the hallway . . .")
                            roomHallwayC()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")

            else:
                print("You succeeded in stealthily taking him down. Now what?")
                while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body. Sadly, nothing useful was found. What now?")
                            bodyCheck = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find a throwing star!")
                            roomChecks = 1
                            user.strength = user.strength + 2
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                        if direction == north:
                            print("Heading to the cells above . . .")
                            room9and10()
                            rooms = 0
                        elif direction == south:
                            print("Heading to the cells below . . .")
                            room121314()
                            rooms = 0
                        elif direction == east:
                            print("Heading to the hallway . . .")
                            roomHallwayC()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")



        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body. Sadly, nothing useful was found. What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find a throwing star!")
                        roomChecks = 1
                        user.strength = user.strength + 2
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to the cells above . . .")
                        room9and10()
                        rooms = 0
                    elif direction == south:
                        print("Heading to the cells below . . .")
                        room121314()
                        rooms = 0
                    elif direction == east:
                        print("Heading to the hallway . . .")
                        roomHallwayC()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")


            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body. Sadly, nothing useful was found. What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find a throwing star!")
                        roomChecks = 1
                        user.strength = user.strength + 2
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                         print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading to the cells above . . .")
                        room9and10()
                        rooms = 0
                    elif direction == south:
                        print("Heading to the cells below . . .")
                        room121314()
                        rooms = 0
                    elif direction == east:
                        print("Heading to the hallway . . .")
                        roomHallwayC()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == north:
                print("Heading to the cells above . . .")
                room9and10()
                rooms = 0
            elif direction == south:
                print("Heading to the cells below . . .")
                room121314()
                rooms = 0
            elif direction == east:
                print("Heading to the hallway . . .")
                roomHallwayC()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")
def room15():
    if roomCheck(15):
        roomWrite(15)
        print('''
        You enter a dining room that seems to be quiet and empty. Would you like to explore around?
        ''')
        if userinput == yes:
            print("You searched the room and managed to find a pair of metal grieves!")
            user.strength = user.strength + 12

        else:
            print("Time to exit the room. What direction are we going?")
            rooms = 1
            while rooms != 0:
                if direction == "east":
                    print("Heading to room 2 . . .")
                    roomHallwayA()
                    rooms = 0
                elif direction == "west":
                    print("Heading to room 15 . . .")
                    room7()
                    rooms = 0
                else:
                    print("You cannot enter this area. Try again.")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == "east":
                print("Heading to room 2 . . .")
                roomHallwayA()
                rooms = 0
            elif direction == "west":
                print("Heading to room 15 . . .")
                room7()
                rooms = 0
            else:
                print("You cannot enter this area. Try again.")
def room16():
    if roomCheck(16):
        roomWrite(16)
        print('''
        You slip into the small room and are met with two of the trolls
        that you recognize as those that stabbed you and knocked you unconscious during the attack on
        your village and the castle. They helped to kidnap your brother. What are we going to do?!"
        ''')
        npcStrength = 54
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            If you're lucky, you can get the upperhand. Let's see what you've got!
            ''')
            if sneakChecker(npcStrength) == False:
                print("You did not succeed in sneaking up on the Terrible Troll Twins. Time to do this the old fashioned way!")
                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received a shiny key, a victory shield, a health potion, and a sturdy sword. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 50
                            user.health = user.health + 15
                            user.key = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You didn't manage to find anything of use. Now what?")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == west:
                            print("Heading to the hallway . . .")
                            roomHallwayC()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check their bodies and received a shiny key, a victory shield, a health potion, and a sturdy sword. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 50
                            user.health = user.health + 15
                            user.key = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You didn't manage to find anything of use. Now what?")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == west:
                            print("Heading to the hallway . . .")
                            roomHallwayC()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")
            else:
                print("You succeeded in stealthily taking them down. Now what?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a shiny key, a victory shield, a health potion, and a sturdy sword. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 50
                        user.health = user.health + 15
                        user.key = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything of use. Now what?")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == west:
                        print("Heading to the hallway . . .")
                        roomHallwayC()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")


        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a shiny key, a victory shield, a health potion, and a sturdy sword. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 50
                        user.health = user.health + 15
                        user.key = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything of use. Now what?")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == west:
                        print("Heading to the hallway . . .")
                        roomHallwayC()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and received a shiny key, a victory shield, a health potion, and a sturdy sword. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 50
                        user.health = user.health + 15
                        user.key = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You didn't manage to find anything of use. Now what?")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == west:
                        print("Heading to the hallway . . .")
                        roomHallwayC()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == west:
                print("Heading to the hallway . . .")
                roomHallwayC()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")
def room19():
    if roomCheck(19) and user.key == 1:
        roomWrite(2)
        print('''
        You use the key to softly open the door. A gasp escaping your lungs as you see your
        brother sitting on a jagged bench in front of you. His body was covered in sweat and
        discolored. Breath coming in heaving gasps.

        “Hannibal! You’re okay!”

        He looks up at you, face dark and weary. His eyes are cloaked in black.

        “It took you long enough…” he whispered, slowly standing up. Something seemed off about him.
        He's acting incredibly bizarre.

        "Hannibal is gone, youngling. My name is Belsnickel, the destroyer of men."

        He was possessed by the demon belsnickel.

        You must choose to sacrifice your life or end your brother’s to survive.

        ''')
        npcStrength = 500
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "sacrifice":
            print('''
            "Brother, I can't fight you. You're my blood. I can't do that."

            He smirked at you and made a sudden movement.

            Everything went black.

            It was all over. And for what?
            ''')

            print("GAME OVER . . .")


        elif response == "ATTACK":
            print('''
            You chose to charge into an attack... Against your brother... It... It doesn't look like it will be too good.
            ''')
            if attackSequence(npcStrength):
                print("...You... You managed to defeat him. The fight was difficult. You fell down to your knees in front of him. The demon was gone...")
                print("But the longer you look... the more you notice his stillness. Your brother... He's... He's gone.")
                print("It's all over now... What is there left to do?")
            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("...You... You managed to defeat him. The fight was difficult. You fell down to your knees in front of him. The demon was gone...")
                print("But the longer you look... the more you notice his stillness. Your brother... He's... He's gone.")
                print("It's all over now... What is there left to do?")
        elif response == "exorcism":
            print("You decided to make an attempt at exorcism. Pulling out the Bible you have stashed in your armor, you begin to recite...")
            rolled = roll()
            if (user.intelligence + rolled) >= 12:
                print("You were successful! You managed to save your brother's life!")
            else:
                print("It was not successful... Belsnickel burned your brother's body in retaliation as he fled.")
    else:
        print("It seems that the door is locked and you need to find a key. Where do you want to go now?")
        rooms = 1
        while rooms != 0:
            if direction == west:
                print("Heading to the hallway . . .")
                roomHallwayC()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")

def roomHallwayA():
    if roomCheck(20):
        roomWrite(20)
        print('''
        You entered the hallway and hear footsteps pacing along it. How are you going to approach this?!
        ''')
        npcStrength = 35
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            You are going to attempt to sneak up on the guard in the hallway. Let's see if it's successful!
            ''')
            if sneakChecker(npcStrength) == False:
                print("You did not succeed in neutralizing the guard. You must now attack!")
                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body and unluckily found nothing. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 3
                            user.health = user.health + 15
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find some matches and a couple small knives. Luckily, you also found two health potions!")
                            roomChecks = 1
                            user.strength = user.strength + 2
                            user.health = user.health + 30
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading further down the hall . . .")
                            room1()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 19 . . .")
                            room19()
                            rooms = 0
                        elif direction == west:
                            print("Heading to room 15 . . .")
                            room15()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")

                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body and unluckily found nothing. What now?")
                            bodyCheck = 1
                            user.strength = user.strength + 3
                            user.health = user.health + 15
                        elif userinput == "room" and roomChecks == 0:
                            print("You decided to check the room. You managed to find some matches and a couple small knives. Luckily, you also found two health potions!")
                            roomChecks = 1
                            user.strength = user.strength + 2
                            user.health = user.health + 30
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                            print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == north:
                            print("Heading further down the hall . . .")
                            room1()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 19 . . .")
                            room19()
                            rooms = 0
                        elif direction == west:
                            print("Heading to room 15 . . .")
                            room15()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")
            else:
                print("You succeeded in stealthily taking him down. Now what?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and unluckily found nothing. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 3
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find some matches and a couple small knives. Luckily, you also found two health potions!")
                        roomChecks = 1
                        user.strength = user.strength + 2
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading further down the hall . . .")
                        room1()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 19 . . .")
                        room19()
                        rooms = 0
                    elif direction == west:
                        print("Heading to room 15 . . .")
                        room15()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")


        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and unluckily found nothing. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 3
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find some matches and a couple small knives. Luckily, you also found two health potions!")
                        roomChecks = 1
                        user.strength = user.strength + 2
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading further down the hall . . .")
                        room1()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 19 . . .")
                        room19()
                        rooms = 0
                    elif direction == west:
                        print("Heading to room 15 . . .")
                        room15()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and unluckily found nothing. What now?")
                        bodyCheck = 1
                        user.strength = user.strength + 3
                        user.health = user.health + 15
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. You managed to find some matches and a couple small knives. Luckily, you also found two health potions!")
                        roomChecks = 1
                        user.strength = user.strength + 2
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading further down the hall . . .")
                        room1()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 19 . . .")
                        room19()
                        rooms = 0
                    elif direction == west:
                        print("Heading to room 15 . . .")
                        room15()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == north:
                print("Heading further down the hall . . .")
                room1()
                rooms = 0
            elif direction == east:
                print("Heading to room 19 . . .")
                room19()
                rooms = 0
            elif direction == west:
                print("Heading to room 15 . . .")
                room15()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")

def roomHallwayB():
    if roomCheck(21) and user.key == 1:
        print('''
        You're still venturing down the hallway, but you luckily don't hear a guard. To your right, you hear rustling in a cell.
        Voices are coming from your side and further down the hall. Two men were talking through their cells when you looked up. The
        two men begin beckoning you.
        Master?
        You lock eyes with your servant Dwight.
        "Dwight! You're still alive! Thank God!"
        A smile flit across Dwight's sunken in face.
        "It's so good to see you, Master! A few of us made it out! Oscar is in the cell next to me and Jimothy got taken to a different cell."
        "I will get you men out of here!"
        He locked eyes with me.
        "Do whatever you must, Master. But please, please save your brother! He's not well."

        Shock echoes through your body.

        "You've seen him???"

        "Yes, Master, he's not well.
        ''')

        roomWrite(21)
        npcStrength = 50
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "free":
            print('''
            You chose to free these men! This will help in any upcoming battles you may have! Now, quickly, what direction must we go?
            ''')
            user.strength = user.strength + 100
            rooms = 1
            while rooms != 0:
                if direction == north:
                    print("Heading further down the hall . . .")
                    roomHallwayC()
                    rooms = 0
                elif direction == south:
                    print("Heading back up the hall . . .")
                    roomHallwayA()
                    rooms = 0
                else:
                    print("This direction is invalid. Try again!")

        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and unluckily found nothing. You're a heartless murderer.......... What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. Nothing of value")
                        roomChecks = 1
                        user.strength = user.strength + 2
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading further down the hall . . .")
                        roomHallwayC()
                        rooms = 0
                    elif direction == south:
                        print("Heading back up the hall . . .")
                        roomHallwayA()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

            else:
                print("You must roll again.")
                while attackSequence(npcStrength) == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and unluckily found nothing. You're a heartless murderer.......... What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. Nothing of value")
                        roomChecks = 1
                        user.strength = user.strength + 2
                        user.health = user.health + 30
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == north:
                        print("Heading further down the hall . . .")
                        roomHallwayC()
                        rooms = 0
                    elif direction == south:
                        print("Heading back up the hall . . .")
                        roomHallwayA()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == north:
                print("Heading further down the hall . . .")
                roomHallwayC()
                rooms = 0
            elif direction == south:
                print("Heading back up the hall . . .")
                roomHallwayA()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")

def roomHallwayC():
    if roomCheck(22):
        roomWrite(22)
        print('''
        Venturing further down the hall, you come across another guard
        ''')
        npcStrength = 35
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "SNEAK":
            print('''
            You are going to attempt to sneak up on the guard in the hallway. Let's see if it's successful!
            ''')
            if sneakChecker(npcStrength) == False:
                print("You did not succeed in neutralizing the guard. You must now attack!")
                if attackSequence(npcStrength):
                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body and unluckily found nothing. What now?")
                            bodyCheck = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You found nothing. Now what?")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == South:
                            print("Heading back up the hall . . .")
                            roomHallwayB()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 16 . . .")
                            room16()
                            rooms = 0
                        elif direction == west:
                            print("Heading to room 11 . . .")
                            room11()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")


                else:
                    print("You must roll again.")
                    while attackSequence(npcStrength) == False:
                        npcStrength = npcStrength - user.strength
                        attackSequence(npcStrength)

                    print("Congratulations! What would you like to do now?")
                    while room == 4:
                        ###get input
                        if userinput == "body" and bodyCheck == 0:
                            print("You decided to check his body and unluckily found nothing. What now?")
                            bodyCheck = 1
                        elif userinput == "room" and roomChecks == 0:
                            print("You found nothing. Now what?")
                            roomChecks = 1
                        elif userinput == "body" and bodyCheck == 1:
                            print("Their bodies have been checked. Try again.")
                        elif userinput == "room" and roomChecks == 1:
                            print("The room has been checked. Try again.")
                        elif userinput == "leave":
                            print("I see that you wish to leave the room. Let's go!")
                            room = 0
                        else:
                            print("Input is invalid. Try again.")

                    print("What direction would you like to go?")
                    rooms = 1
                    while rooms != 0:
                        if direction == South:
                            print("Heading back up the hall . . .")
                            roomHallwayB()
                            rooms = 0
                        elif direction == east:
                            print("Heading to room 16 . . .")
                            room16()
                            rooms = 0
                        elif direction == west:
                            print("Heading to room 11 . . .")
                            room11()
                            rooms = 0
                        else:
                            print("This direction is invalid. Try again!")
            else:
                print("You succeeded in stealthily taking him down. Now what?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and unluckily found nothing. What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You found nothing. Now what?")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == South:
                        print("Heading back up the hall . . .")
                        roomHallwayB()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 16 . . .")
                        room16()
                        rooms = 0
                    elif direction == west:
                        print("Heading to room 11 . . .")
                        room11()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")


        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and unluckily found nothing. What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You found nothing. Now what?")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == South:
                        print("Heading back up the hall . . .")
                        roomHallwayB()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 16 . . .")
                        room16()
                        rooms = 0
                    elif direction == west:
                        print("Heading to room 11 . . .")
                        room11()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

            else:
                print("You must roll again.")
                while attackSequence == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check his body and unluckily found nothing. What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You found nothing. Now what?")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == South:
                        print("Heading back up the hall . . .")
                        roomHallwayB()
                        rooms = 0
                    elif direction == east:
                        print("Heading to room 16 . . .")
                        room16()
                        rooms = 0
                    elif direction == west:
                        print("Heading to room 11 . . .")
                        room11()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == South:
                print("Heading back up the hall . . .")
                roomHallwayB()
                rooms = 0
            elif direction == east:
                print("Heading to room 16 . . .")
                room16()
                rooms = 0
            elif direction == west:
                print("Heading to room 11 . . .")
                room11()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")
def room9and10():
    if roomCheck(9) and user.key == 1:
        print('''
        Two of your men are in the cells. Will you help them?
        ''')
        roomWrite(21)
        npcStrength = 50
        room = 4
        bodyCheck = 0
        roomChecks = 0
        if response == "free":
            print('''
            You chose to free these men! This will help in any upcoming battles you may have! Now, quickly, what direction must we go?
            ''')
            user.strength = user.strength + 100
            rooms = 1
            while rooms != 0:
                if direction == south:
                    print("Heading to room 11 . . .")
                    room11()
                    rooms = 0
                else:
                    print("This direction is invalid. Try again!")

        elif response == "ATTACK":
            print('''
            You chose to charge into an attack. Will you be successful?
            ''')
            if attackSequence(npcStrength):
                print("Congratulations! What would you like to do now?")
                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and unluckily found nothing. You're a heartless murderer.......... What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. Nothing of value")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == south:
                        print("Heading to room 11 . . .")
                        room11()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

            else:
                print("You must roll again.")
                while attackSequence(npcStrength) == False:
                    npcStrength = npcStrength - user.strength
                    attackSequence(npcStrength)

                print("Congratulations! What would you like to do now?")

                while room == 4:
                        ###get input
                    if userinput == "body" and bodyCheck == 0:
                        print("You decided to check their bodies and unluckily found nothing. You're a heartless murderer.......... What now?")
                        bodyCheck = 1
                    elif userinput == "room" and roomChecks == 0:
                        print("You decided to check the room. Nothing of value")
                        roomChecks = 1
                    elif userinput == "body" and bodyCheck == 1:
                        print("Their bodies have been checked. Try again.")
                    elif userinput == "room" and roomChecks == 1:
                        print("The room has been checked. Try again.")
                    elif userinput == "leave":
                        print("I see that you wish to leave the room. Let's go!")
                        room = 0
                    else:
                        print("Input is invalid. Try again.")

                print("What direction would you like to go?")
                rooms = 1
                while rooms != 0:
                    if direction == south:
                        print("Heading to room 11 . . .")
                        room11()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")
        else:
            print("Response is invalid. Please try again!")


    else:
        print('''
        This room has already been visited. What direction would you like to head in?
            ''')
        rooms = 1
        while rooms != 0:
            if direction == south:
                print("Heading to room 11 . . .")
                room11()
                rooms = 0
            else:
                print("This direction is invalid. Try again!")
def room121314():
    if roomCheck(12):
        roomWrite(12)
        print('''
        In front of you are three cells with skeletons in them. Do you want to explore them?
        ''')
        if response == "yes":
            print('''
            You chose to explore their cells. Luckily, you found an enchanted ring! Let's move on!
            ''')
            user.strength = user.strength + 10
            rooms = 1
            while rooms != 0:
                if direction == north:
                    print("Heading to room 11 . . .")
                    room11()
                    rooms = 0
                else:
                    print("This direction is invalid. Try again!")

        else:
            print('''
            You chose to move on. Let's get going! What direction?
            ''')
            print("What direction would you like to go?")
            rooms = 1
            while rooms != 0:
                    if direction == north:
                        print("Heading to room 11 . . .")
                        room11()
                        rooms = 0
                    else:
                        print("This direction is invalid. Try again!")

def main():
    introduction()
    room3()

if __name__ == '__main__':
    main()
