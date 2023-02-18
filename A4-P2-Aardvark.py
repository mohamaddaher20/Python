# #Program 2 – The Itsy Bitsy Aardvark
# #Description: Design and develop a program that presents the user with a “Mad Libs” type game, where a random 
# # choice of words are read from a file, then interjected into a story read from another file.

# #Student #: 0459521     
# #Student Name: Mohamad Taha Daher  

#     # YOUR CODE STARTS HERE, each line must be indented (one tab)

import csv
#Define a function for the user options 
def choiceletter(counter):                
    alphabetList=["a","b","c","d","e"]
    choiceLetter=alphabetList[counter]
    return choiceLetter
#Function to check user input.
def alphabets(position):                       
    alphabetList=["a","b","c","d","e"]
    alphabetSelected=alphabetList[position]
    return alphabetSelected

def main(): 
    print("\nThe Itsy Bitsy Aardvark")
    
    fileName="Files\\the_choices_file.csv"
    accessMode="r"

    words=[]
    with open(fileName,accessMode) as secondaryFile: 
        wordChoiceList=csv.reader(secondaryFile)
        for row in wordChoiceList:
            print("\nPlease choose ",end="")
            counter=-1
            for choices in row:
                if counter==-1:
                    print (choices)
                    counter+=1
                else:
                    choiceLetter=choiceletter(counter)   
                    print("\t\t\t"+choiceLetter+") "+choices)   #Print options choices for user to choose.
                    counter+=1
            whileterminator=0
            while whileterminator==0:
                wordchosen=input("Word chosen (a-{0}): ".format(choiceLetter))
                for letters in range(counter):
                    if wordchosen.lower()==alphabets(letters):
                        words.append(row[letters+1])      #Create a list of words that has been chosen 
                                                                #by the user.
                        whileterminator+=1
                        break
                if whileterminator==0:
                    print("Invalid input. Please choose single letter only.")
        print("")
    
    #Convert the text from strings to words to add to the element list 
    fileStory="Files\\the_story_file.txt"
    accessmode="r"
    with open(fileStory,accessmode) as secondaryfileStory:
        storywithblanks=secondaryfileStory.readline()
        outputfile="The_Itsy_Bitsy_Aardvark.txt"
        with open(outputfile,"w") as outputfilesave:
            while storywithblanks:
                storywithblankslist=storywithblanks.split()  
                                                             
                for x in range(len(storywithblankslist)):
                    wordsList=list(storywithblankslist[x])   
                    if wordsList[0]=="_":
                        replacewordnumber=int(wordsList[1])
                        storywithblankslist[x]=words[replacewordnumber-1].upper() #Replace words chosen by user to the blanks.  
                storywithblanks=secondaryfileStory.readline()    
                finalstory=" ".join(storywithblankslist)      
                print(finalstory)  #Print the story on the screen with chosen words in blanks.                            
                outputfilesave.write(finalstory+"\n")  

    # YOUR CODE ENDS HERE

main()
