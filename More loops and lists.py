# Example of repeating of the entir program.
# call main() inside of a loop, tied to user if they want to repeat or not.

# usercontinued = "y"

# def main():
#   sqfeetpergallon = 150
  
#   print("welcome to the paintshop calculator")
#   areaofroom = int(input("Please enter the total area of your room: "))

#   numofgallons = areaofroom / sqfeetpergallon

#   print("You need {0:.2f} gallons to paint your {1} sq ft room".format(numofgallons, areaofroom))


# while(usercontinued.lower() == "y"):      # To t
#   main()
#   usercontinued = input("do you want to enter more rooms (y/n)")

# print("Thank you for shopping at my paintshop")

##############################################################################

# Example 2 - Paraller Lists

# hockeyteams = []

# for i in range(2):
#   nameofteam = input("please enter a name of a hockey team: ")
#   hockeyteams.append(nameofteam)
#   hockeyteams.append(int(input("How many points does the have? ".format(nameofteam))))
  
# print(hockeyteams)

# for j in range (0, 6, 2): ###
#   print(hockeyteams[j] + "-" + str(hockeyteams[j + 1]))

####################################################################################

# Example 3 - easier parallel list example 

hockeyteamnames = []
hockeyteamscores = []

for i in range(2):
  nameofteam = input("please enter a name of a hockey team: ")
  hockeyteamnames.append(nameofteam)
  hockeyteamscores.append(int(input("How many points does the have? ".format(nameofteam))))
  
print(hockeyteamnames)
print(hockeyteamscores)

for j in range(3):
  print(hockeyteamnames[j] + "-" + str(hockeyteamscores[j]))

# for j in range (0, 6, 2): ###
#   print(hockeyteams[j] + "-" + str(hockeyteams[j + 1]))

#################################################################################

# Example 4 - Strings like lists

# name = "Taha"

# for i in range(len(name)):
#   print(name[i])      # It will print one letter at a time

#################################################################################

# Example 5 - Loops without indexes

# animals = ["elephant", "penguin", "Aardvark", "Tiger", "Turtle"]

# for animal in animals:
#   print(animal)




# for animal in "Bazoka":
#   print(animal)



# # List in a list 
# letters = [[1,2,3], "B", "C"]
# print(letters[0][2])