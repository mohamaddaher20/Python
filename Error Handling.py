import random

def main():
    lowerBound = 1
    upperBound = 100

    secretNumber = random.randint(lowerBound, upperBound)
    guessCounter = 0

    print("Number Guessing Game/n")

    while True:
        userGuess = input("Please enter a number between {0} and {1}".format(lowerBound, upperBound))
        guessCounter += 1
        try:
            if int(userGuess) > upperBound or int(userGuess) < lowerBound:
                print("OUT OF RANGE! Please enter a number between {0} and {1}.".format(lowerBound, upperBound))
            elif int(userGuess) == secretNumber:   #GOT IT!
                print("\nYOU GOT IT! The secret number was {0} and you guessed it correctly!".format(secretNumber))
                break
            elif int(userGuess) > secretNumber:
                print("NOPE! The secret number is LOWER than {0}".format(userGuess))
            elif int(userGuess) < secretNumber:
                print("NOPE! The secret number is HIGHER than {0}".format(userGuess))
        except ValueError:  # Specific error
            print("You must enter a valid number")
        except IndexError:
            print("Index error occured")
        except: # Not specific 
            print("An error occured")
        #except IndexError as err:
        #print(err)


main()