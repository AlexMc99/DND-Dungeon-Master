def getplayerdata(file1):
    name = getName(file1)
    position = getPosition(file1)
    strength = getstrength(file1)
    intelligence = getintell(file1)
    money = getGold(file1)
    potions = getHPP(file1)
    lists = [name, position, strength, intelligence, money, potions]
    print(*lists, sep = "\n")

def getName(lines):
    return lines[0]

def getPosition(lines):
    return lines[1]

def getstrength(lines):
    return lines[2]

def getintell(lines):
    return lines [3]

def getHP(lines):
    return lines[4]

def getGold(lines):
    return lines[5]

def getHPP(lines):
    return lines[6]

def updatePosition(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[0] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()
        
def updateStrength(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[1] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()
        
def updateIntell(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[2] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()

def updateHP(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[3] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()

def updateGold(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[4] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()

def updatePotions(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[5] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()

def updateHPP(newLine, filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines[6] = newLine
    with open(filename, "w") as file:
        file.writelines(lines)
    file.close()
    
 
userinfo = input("Press 1 if you have save data and 0 if you do not: ")
print(userinfo)
if userinfo == "0":
    print("This line was hit!\n")
    name = input("Please enter name of character: ")
    strength = "10"
    intelligence = "10"
    money = "500"
    potions = "0"
    position = "(0,0)"
    hp ="100"
    
    file1 = open("save.txt","w")
    
    file1.write(name)
    file1.write("\n")
    file1.write(position)
    file1.write("\n")
    file1.write(strength)
    file1.write("\n")
    file1.write(intelligence)
    file1.write("\n")
    file1.write(hp)
    file1.write("\n")
    file1.write(money)
    file1.write("\n")
    file1.write(potions)
    file1.write("\n")

    file1.close()
    
else:
    #filename = "save.txt"
    file1 = open("save.txt","r")
    #lines = file1.readlines()
    #updateHPP("60", filename)
    #file1.close()


    lines = file1.readlines()
    getplayerdata(lines)

