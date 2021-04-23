import random

room = 1
health = 100
strength = random.randrange(11)
intelligence = random.randrange(11)
gold = 2000

class Player:
    def __init__(self, name, strength, intelligence, health, gold, room):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.health = health
        self.gold = gold
        self.room = room

    @classmethod
    def from_input(cls):
        return cls(
            input("What is your name, adventurer? "),
            strength,
            intelligence,
            health,
            gold,
            room
        )

def main():
    user = Player.from_input()

    print(user.gold)
    if user.gold == 2000:
        user.gold = user.gold - 100
        print(
            user.name,
            user.strength,
            user.intelligence,
            user.health,
            user.gold,
            user.room
        )

if __name__ == "__main__":
    main()
