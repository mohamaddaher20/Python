# Write a program that allows the user to enter the number of hours they worked this week and the dollar amount they make per hour. 

# Use these values to calculate the amount of money they made this week. 

# If the # of hours exceeds 40 in a week, include the amount of overtime pay they made in the total. 

# Overtime pays time-and-a-half (1.5X) the usual hourly wage, and only apply to the # of hours worked over 40. 

#Variables 



#Input 
hourlyrate = float(input("Please enter your hourlyrate: "))
numhoursworked = float(input("please enter your total hours worked: "))

#calculation 
if numhoursworked <= 40:
    totalpay = numhoursworked * hourlyrate          # This is the regular pay 

else: 
    regpay = hourlyrate * 40                        #calc amount for first 40 hours 
    overtimehours = numhoursworked - 40
    overtimerate = hourlyrate * 1.5
    overtimepay = overtimehours * overtimerate
    #add total together to get final amount 
    totalpay = regpay + overtimepay 

print(totalpay)



