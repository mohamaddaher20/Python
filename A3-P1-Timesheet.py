#Program 1 – Timesheet  
#Student #: 0459521    
#Student Name: Mohamad Taha Daher  

# Design and write a program that accepts the number of hours worked on each of 
# five work days from the user, then displays different information calculated about
# those entries as output.

# Prompt the user to enter the five daily hours worked amounts and store them in the program. 
# Determine the day(s) on which the most hours were worked and display the day(s) and hours onscreen. 
# Calculate and display both the total and the daily average of hours worked.
# Display a list of all days that had insufficient hours, which is defined as less than 7 hours.

# Function for max and counter value
def maximum_hours(hours):
    max_value = 0
    counter_value = 0
    for i in range(5):
        if max_value < hours[i]:
            max_value = hours[i]
            counter_value = i +1
    return max_value, counter_value

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Initialize variables
    hours = []  # Empty list
    average = 5
    max_value = 0
    counter_value = 0

    # Used for loop because I have given how many times to loop
    for counter in range(5):
        hoursworked = int(input("Enter hours worked on day #{0}: ".format(counter +1)))     # +1 so it does not start on day 0
        hours.append(hoursworked)       # Add to my empty list

    max_value, counter_value = maximum_hours(hours)     # Call the function

    # To find the highest number of hours worked
    print("The most hours worked was on: Day #{0} when you worked {1} hours.".format(counter_value, max_value))

    # To find the the total hours worked
    print("The total number of hours worked was: {0}".format(sum(hours)))

    # To find the average of hours worked 
    print("The average number of hours worked each day was: {0}".format(sum(hours)/ average))

    # To find the hours worked that are less than 7
    print("Days you slacked off (i.e. worked less than 7 hours):") 

    # For loop to for hours that are less than 7
    for i in range(5):
        if hours[i] < 7:
            print("Day #{0}: {1} hours".format(i+1, hours[i]))

    # YOUR CODE ENDS HERE

main()