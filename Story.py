def introduction():
    return '''
    It has been a long journey, but it will pay off soon. Do you rember what
    happened?
    ...

    Your brother was kidnapped by the King of Trolls duringan invasion on your
    homeland, the Kingdom of Glott. Cattle was killed, homes were burned, and
    innocent lives were lost in the slaughter. Your brother, King Consort
    Hannibal, married to Queen Regnant Demetria, was kidnapped during the
    invasion.

    You have been venturing through the marshy, barbaric Land of Boog in hopes
    of finding yourbrother. It has been exhausting. You have been ambushed,
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

def room3_yes():
    return '''
    You decided to take the torch.

    It will help to illumiate the pathway for you.

    You go through the door, not knowing what awaits you on the other side.
    '''

def room3_no():
    return '''
    You decided not to take the torch.

    Your endeavor will be harder with your limited field of sight.

    You go through the door, not knowing what awaits you on the other side.
    ''' 

def room4_intro():
    return '''
    You here a creaking noise down the hallway, what do you do?
    '''

def room4_sneak():
    return '''
    You chose to quietly venture down the hall, peeking around the corner as you
    approach.
    '''

def room4_sneak_success():
    return '''
    You stealthily managed to subdue him.

    For the moment, you are safe. You managed to neutralize the threat in the
    room. What do you do?
    '''

def room4_sneak_fail():
    return '''
    You were unable to stealthily subdue him.

    The enemy notices you and you prepare for a fight.
    '''

def room4_attack():
    return '''
    You chose to charge into an attack.
    '''

def room4_attack_success():
    return '''
    The atttack was successful and you took him down easily.

    For the moment, you are safe. You managed to neutralize the threat in the
    room. What do you do?
    '''

def room4_attack_fail():
    return '''
    You were unable to subdue him with your attack.

    You prepare to attack again.
    '''

def room4_explore():
    print('''
    You chose to explore the room.

    That was a wonderful idea! Under a pile of debris, you managed to find a
    pile of 20 pieces of gold and a helmet.

    You move on to the next room.
    ''')

def room4_next():
    print('''
    You chose to move on to the next room.
    ''')

def room2_intro():
    print('''
    You hear two voices and the conversation immediately cuts short upon your
    entry. You look up and see a large toad and a miniscule troll standing at a
    table in the center of the room, their eyes quickly dart to you. You can see
    fear flicker across their faces.

    "Wh-who are you?!” the Toad demands, voice quivering.

    What do you do?
    ''')

def room2_attack():
    print('''
    You chose to antagonize.

    You yell, "I’m here to destroy you!"

    The enemy stands up and you prepare for battle.
    ''')

def room2_attack_success():
    print('''
    The atttack was successful and you took down the enemy.

    What do you do next?
    ''')
