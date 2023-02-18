#Program 1 – Hipster's Local Vinyl Records

#Hipster’s Local Vinyl Records sell and hand-deliver vinyl records to their customers.

#Delivery is charged at a rate of $15 per kilometer. 

#All purchases are subject to a 14% sales tax.

#Because this store loves retro technology, you have been asked to develop a console application solution that will enable 
#the company’s retail staff to calculate receipts. Begin by designing your solution to this problem in pseudocode, which 
#will be submitted along with the program. The program user must be able to input the customer's name, the number of 
#kilometers distance, and the cost of any records purchased. Once the input is provided, 
#the program will display the #customer's name and three calculated costs: 
# delivery cost, records cost (plus tax) and total cost, as shown below.
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #print a welcome message to the customer
    print("Welcome to the Hipster's Local Vinyl Record!")
    print("Customer order details!\n")

    #Input questions for the customer
    nameofcustomer = input("Please enter your name here: ")
    distanceinkilometers = float(input("Please enter your distance in km: "))
    purchasecost= float(input("Please enter the cost of the purchased record: "\n))

    #Calculation 
    tax = 0.14
    delivery = float(distanceinkilometers * 15)
    recordcost = float(purchasecost * (1 + tax))
    total = float (delivery + recordcost)

    #print total cost for the customer
    print ("{0}, Thank you for your purchase, Your delivery cost is ${1:.2f}, your record cost is ${2:.2f} and the total cost is ${3:.2f}.".format(nameofcustomer,delivery, recordcost, total) )






    # YOUR CODE ENDS HERE

main()