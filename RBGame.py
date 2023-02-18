#Text- based RPG game
#welcome to the game message
#setup info
#prompt user to enter character name
#prompt user to enter a class
#Greet their character and enter the game
#Mock up an encounter with a monster
#Mock up a fight

import random #always at the top




print("Jedi Adventure")
print("Bobla blaw: The Begining\n")

print("Creat a jedi master and adventure through space and time!\n")

gameInstructions = "fight in space, a bottle for control of Endor and surrounding environs\n"
print(gameInstructions)

charName = input("Please enter a name for your jedi character: ")
#print(charName)

charClass = input("please enter your class: ")
#print(charclass)

#charHP = int(input("\tplease enter your hit points: "))
charHP = random.randint(50, 100)

print("You wake up in a huge dark temple.")
print("A hooded figure appears before you and says:")

#Method 3 - string.format
print("Welcome {0}! I can sense you are a {1}.".format(charName, charClass))
monsterName = "Ewok"
monsterDamage = random.randint(15, 25)

print("\nyou board a ship to Naboo. Upon landing, \nyou are stopped by an Imperial battle droid.")
print("it attacks!\n")

userchoice = input("do you wish to fight the" + monsterName + "? (Y/N):")

if userchoice.upper() == "Y": 
    #True
    print("The {0} hits you for {1} damage, ouch!". format(monsterName, monsterDamage))
    charHP = charHP - monsterDamage
    print ("you have {0} hp remaining".format (charHP))

#false
else: 
    print("You run away!!!")

print("Game over")