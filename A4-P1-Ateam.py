#Program 1 – The A-Team
#Description: Design and write a program that reads the text from a provided text file into a list, displays the 
# text on-screen, makes some alterations to the text and outputs the changed text to the screen, then saves the 
# altered text as a new file. 

#Student #: Mohamad Taha Daher     
#Student Name: 0459521  

import random

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    # Define file and access variables
    fileName = "Files\\ateam_Original.txt"
    accessMode = "r"

    # Open connection to my targeted file
    myFile = open(fileName, accessMode)
    outputFile = open("outputdata.txt","w")

    # Read lines
    fileRead = myFile.readlines()
    outputdata = []
    lineNumber = 1
    for line in fileRead:
        if len(line) > 20:
            outputdata.append(str(lineNumber)+": "+line.lower())
        else:    
            outputdata.append(str(lineNumber)+": "+line.upper())
        lineNumber += 1
     
    length = len(fileRead)
    lineToRemove = random.randint(0,length-1)
    outputdata.pop(lineToRemove)
    for line in outputdata:
        print(line,end="")
        outputFile.write(line)
    
    # close the file
    myFile.close()
    outputFile.close()

    # YOUR CODE ENDS HERE
main()