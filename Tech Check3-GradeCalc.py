# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Initialize variables 
    a=4.0
    b=3.0
    c=2.0
    d=1.0
    f=0

    #Print name of calculator
    print("Grade Point Calculator\n")

    #description of the program
    print("Valid letter grades that can be entered: A, B, C, D, F")
    print("Valid grade modifiers are +, - or nothing")
    print("All letter grades except F can include a + or - symbol")
    print("Calculated grade point value cannot exceed 4.0.")

    # Inputs from the user
    gradeletter = input("please enter a letter grade: ").lower()
    modifier = input("please enter a modifier (+, - or nothing): ")

    # process if letter is A
    if gradeletter == "a":
        value = a 
        if modifier  == "-":
            value = 3.7
    
    # process if letter is B
    elif gradeletter == "b":
        value = b
        if modifier == "+":
                value= 3.3
                if modifier == "-":
                    value = 2.7
            
    
    # process if letter is C
    elif gradeletter == "c":
        value = c
        if modifier == "+":
            value = 2.3
            if modifier == "-":
                value = 1.7
            

    # process if letter is D
    elif gradeletter == "d":
        value = d
        if modifier == "+":
            value= 1.3
            if modifier == "-":
                value=0.7
    
    # process if letter is F
    elif gradeletter == "f":
        value = 0.0

    # If user entered invalid value 
    else:
        value= 0.0
        print("you entered an invalid letter grade")
        
    #output 
    print ("The numeric value is: {0}".format(value))







    # YOUR CODE ENDS HERE

main()
