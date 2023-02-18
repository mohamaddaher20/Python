#Program 2 – Message Redaction

#Student #: 0459521     
#Student Name: Mohamad Taha Daher 

# Description: Design and write a program that removes all desired letters from any 
# user-entered sentence or phrase. Your solution should demonstrate an understanding
# of how to apply list/loop concepts in a program that should: 
 
# Take a sentence or phrase as input,
# Take a comma-separated list of letters to remove as input,
# Replace all occurrences of each target letter in the user-entered sentence, regardless of case sensitivity, with an underscore (“_”) character.
# Display the number of letters removed to the user,
# # The program will keep asking the user to enter a new sentence until the user enters the command ‘quit’.

# Function 
def modify_sentence(lettersList, phrase):
    count = 0
    result = ""
    for letter in phrase:
            if letter in lettersList:
                result = result+"_"
                count = count + 1
            else:
                result = result+letter
    return count, result 

def redact():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
     
    # Initialize variables
    phrase = ""
    letters = ""
    lettersList = []
    result = ""
    count = 0

    # Use while loop instead of for since not specified how many loops to run
    while phrase.lower() != "quit": #control the letter casing
        phrase = input("Type a phrase (or quit to exit program): ").lower() #If they want to run then ask for an input
        if phrase == "quit":
            break   # If they want to quit then stop the program
        letters= input("Type a comma-separated list of letters to redact: ").lower()
        lettersList = letters.split(",")
        
        count, result = modify_sentence(lettersList, phrase)

        # To count the number redacted
        print("Number of letters redacted: {0}".format(count))
        #To show the redacted phrase
        print("Redacted phrase: {0} ".format(result))

def main():
    redact()

    # YOUR CODE ENDS HERE
main()


    