#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 
#Develop a short term loan calculator program as a console application with the following specifications.
#Begin by designing #your solution to this problem in pseudocode, which will be submitted along with the program. 
#If A dollars are borrowed at r% interest compounded weekly to purchase something with weekly payments for n years, then the 
#weekly payment is given by the formula (see assignment doc)
#Write a console application that calculates the weekly payment after the user gives the amount of the loan, interest rate, #and number of years.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Name of the program/output
    print("Weekely Loan Calculator\n")

    #What are the inputs 
    amount = float(input("Please enter the amount you wish to loan: ")) #dollar amount
    interestrate = float(input("Please enter the interest rate (%): ")) #in percent 
    numberofyears = int(input("Please enter how long do you want the loan to be in years: ")) #assume whole years

    #calculation for i first and then sub it into the second formula to find weekely amount
    calculationfori = interestrate/ 5200
    weekelypayment = (calculationfori / (1 -(1 + calculationfori) ** (-52 * numberofyears))) * amount


    #output, what is the weekely amount?
    print("Based on the information provided, you will have to pay a weekely amount of ${0:.2f}.".format(weekelypayment))



    # YOUR CODE ENDS HERE

main()