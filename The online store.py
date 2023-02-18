


#variables
taxrateforalberta = 0.05
taxrateforNSNBON = 0.15
taxrateothers = 0.11

taxtotal = 0.0

print("welcome to the online store!")

# Inputs
country = input("please enter where are you from: ").lower()
ordertotal = float(input("What is the total of your order: $ "))

#process if they are from canada
if country == "canada":
    province = input("Which province are you from: ").lower()

    if province == "alberta":
        taxtotal = ordertotal * taxrateforalberta

    elif province == "ontario" or province =="new brunswick" or province =="nova scotia":
        taxtotal = ordertotal * taxrateforNSNBON

    else:
        taxtotal = ordertotal * taxrateothers

# if not from canada
else: 
    totaltax = ordertotal

print("your total is ${0:.2f}".format(taxtotal))

