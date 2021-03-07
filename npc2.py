import json

npcs = [
    {
        "npcName" : "Hersek",
        "npcStrength" : 50,
        "npcPosition" : {
            "xpos" : 6,
            "ypos" : 6

        },

        "npcGold" : 500,
        "npcPotions" : 2

    },
    {
        "npcName" : "Jareth",
        "npcStrength" : 25,
        "npcPosition" : {
            "xpos" : 2,
            "ypos" : 8

        },

        "npcGold" : 0,
        "npcPotions" : 10

    },
    {
        "npcName" : "Goldenface",
        "npcStrength" : 9001,
        "npcPosition" : {
            "xpos" : 6,
            "ypos" : 9

        },

        "npcGold" : 5300,
        "npcPotions" : 7

    },
    {
        "npcName" : "Burt Macklin",
        "npcStrength" : 53,
        "npcPosition" : {
            "xpos" : 7,
            "ypos" : 2

        },

        "npcGold" : 199,
        "npcPotions" : 0

    },
    {
        "npcName" : "Scranton Strangler",
        "npcStrength" : 1000,
        "npcPosition" : {
            "xpos" : 10,
            "ypos" : 10

        },

        "npcGold" : 9001,
        "npcPotions" : 2

    }
]

with open("npcdata.txt", "w") as file1:
    dtos = json.dumps(npcs)
    file1.write(dtos)

with open("npcdata.txt", "r") as file2:
    dtos = file2.readline()
    npcs = json.loads(dtos)

for character in npcs:
    print(character)
