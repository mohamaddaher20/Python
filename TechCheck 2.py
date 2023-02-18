# Tax Withheld Calculator

# Write a console program that calculates the total amount of tax withheld from an employee’s weekly salary.
# The total withheld tax amount is calculated by combining the amount of provincial tax withheld and the amount of 
# federal tax withheld, minus a per-dependent deduction from the total tax withheld. The user will enter their pre-tax 
# weekly salary amount and the number of dependents they wish to claim. 
# 
# The program will calculate and output the amount of provincial tax withheld, amount of federal tax withheld, the 
# dependent tax deduction, and the user’s final take-home amount.
# Provincial withholding tax is calculated at 6.0%. Federal withholding tax is calculated at 25.0%. 
# The tax deduction for dependents is calculated at 2.0% of the employee’s salary per dependent.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    print("Tax Withheld Calculator\n")

    weekelysalary = float(input("please enter the full amount of your weekely salary: "))
    numofdependents = float (input("How many dependents do you have?: "))

    provtax = 0.06 
    fedtax = 0.25
    dependenttax = 0.02 

    provencialtax = provtax * weekelysalary
    federaltax = fedtax * weekelysalary 
    dependentdeduction = dependenttax * weekelysalary * numofdependents
    totalwithheld = provencialtax + federaltax - dependentdeduction 
    totaltakehome = weekelysalary - totalwithheld

    print("provincial Tax Withheld: ${0:.2f} ".format(provencialtax))
    print("Federal Tax Withheld: ${0:.2f} ".format(federaltax))
    print("Dependent Deduction for {0} dependents: ${1:.2f}".format(numofdependents, dependentdeduction))
    print("Total Withheld: ${0:.2f} ".format(totalwithheld))
    print("Total Take-Home pay: ${0:.2f}".format(totaltakehome))


    # YOUR CODE ENDS HERE
main()