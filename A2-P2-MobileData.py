#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer in the billing period.
# For simplicity, customers are charge based on which range their total data usage falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: W0459521   
#Student Name: Mohamad Taha Daher   

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # print name of the program
    print("Erewhon Mobile Data Plans")

    #Initialize Variables 
    datausage = 0.0
    rateofcharge = 0.0

    #Input data usage from the user 
    datausage = float(input("Enter data usage (MB): "))    

    # calc if data usage less than 200MB   #NOTE no math required it already have a flate rate of $20
    if datausage <= 200:
        rateofcharge = 20

    # calc if data usage between 200 and 500MB. The rate of charge is 0.105. 
    elif datausage > 200 and datausage <= 500:
        rateofcharge = datausage * 0.105

    # calc if datausage between 500MB and 1GB. The rate of charge is 0.110. 
    elif datausage > 500 and datausage <= 1:
        rateofcharge = datausage * 0.110
    
    # calc if data usage over 1GB    #NOTE no math required it already have a flate rate of $118
    elif datausage > 1:
        rateofcharge = 118
    
    # display the output
    #print(rateofcharge)

    # display the output to two decimal places 
    print("Total charge is ${0:.2f}".format(rateofcharge))

    # YOUR CODE ENDS HERE

main()