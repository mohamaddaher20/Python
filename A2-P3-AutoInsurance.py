#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #: w0459521    
#Student Name: Mohamad Taha Daher   

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # print name of the program 
    print("Auto Insurance")

    # Initialize variables 
    age= 0
    vechileprice = 0.0
    monthlyinsurance = 0.0

    # inputs from the user 
    sex= input("Are you 'Male' or 'Female': ").lower()   # convert the user input to lowercase 
    age= int(input("Enter your age: "))
    vechileprice= float(input("Enter the purchase price of the vechile: "))
    
    # process if sex is Male 
    if sex == "male":
    #     #age must be true for both value so use "and"
        if age >= 15 and age < 25:                          
         monthlyinsurance = vechileprice * 0.25 / 12   

         #age must be true for either value so use "or"
         elif age == 25 or age < 40:                            
             monthlyinsurance = vechileprice * 0.17 / 12

         #age must be true for either value so use "or"
         elif age == 40 or age < 70:                             
             monthlyinsurance = vechileprice * 0.10 / 12 
    
     #process if sex is female 
    if sex == "female":
        if age >= 15 and age < 25:                           # Use and 
            monthlyinsurance = vechileprice * 0.20 / 12   
    
        elif age == 25 or age < 40:                            # Use or 
            monthlyinsurance = vechileprice * 0.15 / 12

        elif age == 40 or age < 70:                             # Use or 
            monthlyinsurance = vechileprice * 0.10 / 12
    
    # display output with the monthly insurance 
    print("Your monthly insurance will be ${0:.2f}".format(monthlyinsurance))








    # YOUR CODE ENDS HERE

main()