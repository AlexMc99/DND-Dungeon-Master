import TextScanner

attackSuccess = True
roomChecks = 0
bodyCheck = 0
leave = False
monsterHP = 15

def getRoomCheck():
    global roomChecks
    return roomChecks

def getBodyCheck():
    global bodyCheck
    return bodyCheck

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

def sneakChecker(npcValue, totalDamage, intelligence):
    if (intelligence + totalDamage) > npcValue:
        return True
    else:
        return False

def attackChecker(npcValue, totalDamage, strength):
    if (strength + totalDamage) > npcValue:
        print('strengh: ')
        print(strength)
        print('totalDamage')
        print(totalDamage)
        print('npcValue')
        print(npcValue)
        return True
    else:
        return False

def attackSequence(npcValue, totalDamage, strength):
    if attackChecker(npcValue, totalDamage, strength):
        print("The attack was successful!")
        return True

    else:
        print("The attack was not successful!")
        return False

def getAttackSuccess():
    global attackSuccess
    return attackSuccess
    
def isLeave():
    global leave
    return leave

def introduction():
    return '''
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
    '''

def room3_intro():
    return'''
    Upon entering, you see a torch to your left. Do you wish to take it?
    '''

def room3_interact(userInput):
    if userInput== "Yes" or userInput == "yes":
        return '''
    You decided to take the torch.
    It will help to illumiate the pathway for you.
    You go through the door, not knowing what awaits you on the other side.
    '''
    elif userInput == "No" or userInput == "no":
        return '''
    You decided not to take the torch.
    Your endeavor will be harder with your limited field of sight.
    You go through the door, not knowing what awaits you on the other side.
    '''
    else:
        return '''
    Please enter either yes or no
    '''

def room4_intro():
    return '''
    You here a creaking noise down the hallway, what do you do?
    '''

def room4_interact(response):
    if response == "SNEAK":
        return '''
    You chose to quietly venture down the hall, peeking around the corner as you
    approach. Ahead of you are two men, both heavily armed. You will need to subdue both
    at the same time to be successful. Jareth and Hogarth are two trolls with an attitude problem.
    Can you do it?
    '''
    elif response == "ATTACK":
        return '''
    You chose to charge into an attack. Will you be successful?
    '''
    else:
        return '''
    That is an odd choice. You catch the trolls' eyes. You prepare to atack. Will you be successful?
    '''

def room4_sneak_bool(totalDamage, intelligence):
    if sneakChecker(20, totalDamage, intelligence) == False:
        return False
    else:
        return True

def room4_sneak(totalDamage, intelligence):
    if sneakChecker(20, totalDamage, intelligence) == False:
        return '''
    You did not succeed in taking down Jareth and Hogarth. You must now be forced to battle. Good luck
        '''
    else:
        global attackSuccess
        attackSuccess = False
        return '''
    You succeeded in stealthily taking them down. Now what?
        '''
def room4_attack_bool(totalDamage, strength):
    if attackSequence(25, totalDamage, strength) == False:
        return False
    else:
        return True
        
def room4_attack(totalDamage, strength):
    if attackSequence(25, totalDamage, strength) == False:
        return '''
    You must roll again.
        '''
    else:
        global attackSuccess
        attackSuccess = False
        return '''
    Congratulations you defeated them! What would you like to do now?
        '''

def room4_success(userinput):
    global bodyCheck
    global roomChecks
    print(userinput)
    if "body" in userinput and bodyCheck == 0:
        bodyCheck = 1
        return '''
    You decided to check their bodies and received 1 health potion. What now?
    '''
    elif ("room" in userinput) and roomChecks == 0:
        roomChecks = 1
        return '''
    You decided to check the room. Sadly, there is nothing of value inside. Better luck next time!
    '''
    elif "body" in userinput and bodyCheck == 1:
        return '''
    Their bodies have been checked. Try again.
    '''
    elif "room" in userinput and roomChecks == 1:
        return '''
    The room has been checked. Try again.
    '''
    elif "leave" in userinput:
        global leave
        leave == True
        bodyCheck = 0
        roomCheck = 0
        return '''
    I see that you wish to leave the room. Let's go!
    '''
    else:
        return '''
    Input is invalid. Try again.
    '''

def room_move():
    return '''
    What direction would you like to go?
    '''

def room4_go_north(direction):
    if direction == 'NORTH':
        return '''
    Heading north
    '''
    else:
        return '''
    You cannot enter this area. Try again.
    '''
           
def room2_intro():
    return '''
    You hear two voices and the conversation immediately cuts short upon your
    entry. You look up and see a large toad and a miniscule troll standing at a
    table in the center of the room, their eyes quickly dart to you. You can see
    fear flicker across their faces.

    "Wh-who are you?!” the Toad demands, voice quivering.

    What do you do?
    '''

def room2_interact(response):
    if response == "SNEAK":
        return '''
    You are unable to sneak. They've already spotted you. 
    But, maybe if you're lucky and charismatic enough,
    they will think you're one of them!
    '''
    elif response == "ATTACK":
        return '''
    You chose to charge into an attack. 
    Will you be successful?
    '''
    else:
        return '''
    That is an odd choice. They do not feel like they can trust you. 
    You prepare to attack. Will you be successful?
    '''

def room2_sneak(totalDamage, intelligence):
    if sneakChecker(25, totalDamage, intelligence) == False:
        return '''
    You did not succeed in blending in. 
    You must now be forced to battle. Good luck
    '''
    else:
        global attackSuccess
        attackSuccess = False
        return '''
    You succeeded in stealthily taking them down. Now what?
    '''

def room2_attack(totalDamage, strength):
    if attackSequence(30, totalDamage, strength) == False:
        return '''
    You failed to take them down. You lose 10 HP. You must roll again to keep fighting.
    '''
    else:
        global attackSuccess
        attackSuccess = False
        return '''
    Congratulations! What would you like to do now?
    '''
def room2_move(direction):
    if direction == 'NORTH':
        return '''
    Heading north
    '''
    elif direction == 'SOUTH':
        return '''
    Why would you want to turn back now? Maybe try a different direction
    '''
    elif direction == 'EAST':
        return '''
    Huh... the door is locked. Maybe try a different direction
    '''
    elif direction == 'WEST':
        return '''
    Ouch! You run straight into a wall. Maybe try a different direction
    '''
    else:
        return '''
    This direction is invalid. Try again!
    '''

def room2_success(userinput):
    global bodyCheck
    global roomChecks
    print(userinput)
    if 'body' in userinput and bodyCheck == 0:
        bodyCheck = 1
        return '''
    You decided to check their bodies and received a rusty sword, a rickety helmet, 
    a health potion, and a piece of cloth. What now?
    '''
    elif 'room' in userinput and roomChecks == 0:
        roomChecks = 1
        return '''
    You decided to check the room. You managed to find some matches.
    '''
    elif 'body' in userinput and bodyCheck == 1:
        return '''
    Their bodies have been checked. Try again.
    '''
    elif 'room' in userinput and roomChecks == 1:
        return '''
    The room has been checked. Try again.
    '''
    elif 'leave' in userinput:
        return '''
    I see that you wish to leave the room. Let's go!
    '''
    else:
        return '''
    Input is invalid. Try again.
    '''

def room1_intro():
    return '''
    This room is a dead end. You look around and notice a puddle of goo on the
    floor next to a shackled skeleton. What do you do? Would you like to explore the room
    or move on?
    '''

def room1_interact(response):
    if response == "Yes" or response == "yes":
        return '''
    You decided to check out the goo...

    You chose to approach it. In your overwhelming curiosity, you managed to inhale a
    strange vapor surrounding the ooze. Your intelligence has gone down 2 points and
    your HP has gone down 15 points. The vapor has put you in a daze and made you feel
    sickly. You decide to quickly leave the room and try to get some fresh air.

    '''
    else:
        return '''
    You decided not to approach the toxic goo. That was a good idea.

    It's time to head back to room 2.

    '''



  #  else:
#        print('''
 #       This room has already been visited. What direction would you like to head in?
  #          ''')
   #     rooms = 1
    #    while rooms != 0:
     #       if userinput == "south":
      #          print("Heading to room 2 . . .")
       #         room2()
        #        rooms = 0
         #   else:
          #      print("You cannot enter this area. Try again.")

def main():
    introduction()
    room3()

if __name__ == '__main__':
    main()