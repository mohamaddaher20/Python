#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: W0459521
#Student Name: Mohamad Taha Daher   

#There is a base labour charge of $1000. 
#If the surface (length * width) is over 5000 square feet, add $500. 
#The cost is calculated per square foot. If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
#Each tree requested has a $100 charge. 


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    # Name for the program 
    print("Landscpe Calculator")

    # variables 
    labourcharge = 1000
    fescue = 0.05
    bentgrass = 0.02 
    campus = 0.01
    total = 0.0
    total = total + labourcharge

    # The inputs from the user 
    house= int(input("Enter House Number: "))         # set it to int because house number is a whole number
    depth= float(input("Enter property depth (feet): "))     # set it to float 
    width= float(input("Enter property width (feet): "))     # set it to float just in case if its point number 
    typeofgrass= (input("Enter type of grass (fescue, bentgrass, campus): ")).lower()  # Turn it to lower case 
    numberoftrees= int(input("Enter the number of trees: "))  # set it to int, trees is a whole number 

    # conditional statments begin 
    # use elif statmnet because there is multiple solution to the program

    # process if type of grass is fescue 
    if typeofgrass == "fescue":
        charge = fescue
    
    # process if type of grass is bentgrass 
    elif typeofgrass == "bentgrass":
        charge = bentgrass  

    # process if type of grass is campus 
    elif typeofgrass == "campus":
        charge = campus

    # Calculation for surface Area 
    SA= depth * width 
    total = total + SA * charge

    # add 500 if the SA is over 5000
    if SA > 5000:
        total = total + 500
    
    #total 
    total = total + (numberoftrees * 100)
    
    #output 
    print("Total cost for house {0} is: ${1:.2f}".format(house, total))

    # YOUR CODE ENDS HERE

main()