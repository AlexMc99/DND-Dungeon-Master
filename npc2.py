import json

npcs = [
    {
        "npcName" : "Jareth",
        "npcPosition" : 4,
        "npcGold" : 10,
        "npcHP" : 5,
        "npcStrength" : 5,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 1,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Hogarth",
        "npcPosition" : 4,
        "npcGold" : 5,
        "npcHP" : 5,
        "npcStrength" : 5,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Hob",
        "npcPosition" : 2,
        "npcGold" : 10,
        "npcHP" : 15,
        "npcStrength" : 7,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Gob",
        "npcPosition" : 2,
        "npcGold" : 10,
        "npcHP" : 10,
        "npcStrength" : 7,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 1,
                "strength" : 2
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Glarg",
        "npcPosition" : 2,
        "npcGold" : 0,
        "npcHP" : 8,
        "npcStrength" : 6,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 1,
                "strength" : 1
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Simon",
        "npcPosition" : 2,
        "npcGold" : 1,
        "npcHP" : 10,
        "npcStrength" : 9,
        "npcInventory" : {
            "cloth" : 1,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 1,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Toxic Goo",
        "npcPosition" : 1,
        "npcGold" : 0,
        "npcHP" : 0,
        "npcStrength" : 15,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Lobster Todd",
        "npcPosition" : 7,
        "npcGold" : 0,
        "npcHP" : 10,
        "npcStrength" : 10,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Woodchuck Todd",
        "npcPosition" : 7,
        "npcGold" : 0,
        "npcHP" : 11,
        "npcStrength" : 10,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 1,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 1,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Kevin",
        "npcPosition" : 5,
        "npcGold" : 1,
        "npcHP" : 10,
        "npcStrength" : 2,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 1,
                "strength" : 5
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Michael",
        "npcPosition" : 5,
        "npcGold" : 6,
        "npcHP" : 15,
        "npcStrength" : 10,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 1,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Snef",
        "npcPosition" : 5,
        "npcGold" : 25,
        "npcHP" : 20,
        "npcStrength" : 21,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 1,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Kristo",
        "npcPosition" : 5,
        "npcGold" : 4,
        "npcHP" : 20,
        "npcStrength" : 33,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 1,
                "strength" : 6
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Nick",
        "npcPosition" : 5,
        "npcGold" : 5,
        "npcHP" : 21,
        "npcStrength" : 15,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 1,
                "strength" : 10
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Angry Zoe",
        "npcPosition" : 6,
        "npcGold" : 6,
        "npcHP" : 20,
        "npcStrength" : 25,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 5,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Angry Joey",
        "npcPosition" : 6,
        "npcGold" : 0,
        "npcHP" : 10,
        "npcStrength" : 6,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Merchant Todd",
        "npcPosition" : 8,
        "npcGold" : 500,
        "npcHP" : 100,
        "npcStrength" : 100,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 5,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 1,
                "strength" : 8
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 1,
                "strength" : 9
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 1,
                "strength" : 5
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Guard 1",
        "npcPosition" : 20,
        "npcGold" : 0,
        "npcHP" : 10,
        "npcStrength" : 20,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Guard 2",
        "npcPosition" : 20,
        "npcGold" : 0,
        "npcHP" : 10,
        "npcStrength" : 20,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Guard 3",
        "npcPosition" : 20,
        "npcGold" : 0,
        "npcHP" : 10,
        "npcStrength" : 20,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Guard 4",
        "npcPosition" : 20,
        "npcGold" : 0,
        "npcHP" : 10,
        "npcStrength" : 20,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 1,
                "strength" : 10
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Skeleton 1",
        "npcPosition" : 12,
        "npcGold" : 0,
        "npcHP" : 0,
        "npcStrength" : 0,
        "npcInventory" : {
            "cloth" : 1,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Skeleton 2",
        "npcPosition" : 13,
        "npcGold" : 0,
        "npcHP" : 0,
        "npcStrength" : 0,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Skeleton 3",
        "npcPosition" : 14,
        "npcGold" : 0,
        "npcHP" : 0,
        "npcStrength" : 0,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 1,
                "strength" : 10
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Guard 5",
        "npcPosition" : 11,
        "npcGold" : 10,
        "npcHP" : 31,
        "npcStrength" : 27,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Prisoner 1",
        "npcPosition" : 9,
        "npcGold" : 0,
        "npcHP" : 50,
        "npcStrength" : 50,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Prisoner 2",
        "npcPosition" : 10,
        "npcGold" : 0,
        "npcHP" : 50,
        "npcStrength" : 50,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Prisoner 3",
        "npcPosition" : 10,
        "npcGold" : 0,
        "npcHP" : 50,
        "npcStrength" : 50,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Troublesome Twin 1",
        "npcPosition" : 16,
        "npcGold" : 150,
        "npcHP" : 43,
        "npcStrength" : 37,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Troublesome Twin 2",
        "npcPosition" : 16,
        "npcGold" : 150,
        "npcHP" : 43,
        "npcStrength" : 39,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 1,
            "sword" : {
                "count" : 1,
                "strength" : 25
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 1,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 1,
                "strength" : 25
            }
        }

    },
    {
        "npcName" : "Prisoner 4",
        "npcPosition" : 17,
        "npcGold" : 10,
        "npcHP" : 50,
        "npcStrength" : 50,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Prisoner 5",
        "npcPosition" : 18,
        "npcGold" : 0,
        "npcHP" : 50,
        "npcStrength" : 50,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 0,
                "strength" : 0
            },
            "grieves" : {
                "count" : 0,
                "strength" : 0
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 0,
                "strength" : 0
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

    },
    {
        "npcName" : "Belsnickel",
        "npcPosition" : 19,
        "npcGold" : 500,
        "npcHP" : 250,
        "npcStrength" : 250,
        "npcInventory" : {
            "cloth" : 0,
            "potions" : 0,
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "chestplate" : {
                "count" : 1,
                "strength" : 50
            },
            "grieves" : {
                "count" : 1,
                "strength" : 22
            },
            "helmet" : {
                "count" : 0,
                "strength" : 0
            },
            "matches" : 0,
            "mirror" : 0,
            "ring" : {
                "count" : 0,
                "strength" : 0
            },
            "scarf" : {
                "count" : 0,
                "strength" : 0
            },
            "dagger" : {
                "count" : 0,
                "strength" : 0
            },
            "throwing knives" : {
                "count" : 0,
                "strength" : 0
            },
            "gauntlet" : {
                "count" : 0,
                "strength" : 0
            },
            "sword" : {
                "count" : 0,
                "strength" : 0
            },
            "key" : 0,
            "wand" : {
                "count" : 1,
                "strength" : 50
            },
            "shield" : {
                "count" : 0,
                "strength" : 0
            }
        }

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
