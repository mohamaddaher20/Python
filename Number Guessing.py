


# Prompt user to choose number between 1 -100
# Tell them higher or lower
# count guesses


# What parts you want to repeat you put it in the loop

import random
from traceback import walk_stack 

# Get a random secret number
secretNumber = random.randint(1,100)

#welcome message
print("Welcome to the number gussing game!\n")

guesscounter = 0
userGuess = 0
while(userGuess != secretNumber ):
    #Get number from user
    userGuess = (input("Guess a number between 1-100: "))
    if userGuess.isnumeric() == True and int(userGuess) <= 100 and int(userGuess) >= 1:   # What if the user did not put a number value  OR and 
        userGuess = int(userGuess)       # turn it to integer
        guesscounter += 1     # if you want to count the guesses if they enter a valid number in the range
        # evaluate users guess
        if userGuess == secretNumber:
            print("You Win")

        elif userGuess > secretNumber:
            print("Your guess is too high")

        elif userGuess < secretNumber:
            print("Your number is too low")

    else:
        print("That is not a valid number between 1 and 100. Please try again")

print("End of program")