#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Welcome message
    print("Welcome To Our restaurant!\n")

    #input 
    billamount = int(input("Please enter your bill amount: "))
    taxamount = float(input("please enter a tax amount of 15%: "))
    tipamount = int(input("please enter a tipe value of 20%: "))

    #calc
    tax= 0.15
    tip= 0.20
    taxamount = (billamount * tax)
    tipamount = (billamount * tip)
    total = float(billamount + tipamount + taxamount)

    #output message
    print("Your original bill amount is {0}, your tax is {1:.2f}, your tip is {2:.1f} and your total is {3:.2f}.".format(billamount, taxamount, tipamount, total))
    print("Thank you for shopping!")


    # YOUR CODE ENDS HERE

main()