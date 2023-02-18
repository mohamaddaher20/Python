#Program 3 – Girl Guide Cookies

#Student #: 0459521     
#Student Name: Mohamad Taha Daher

#Description: The organizers of the annual Girl Guide cookie sale event want to raise 
# the stakes on the number of cookies sold and are offering cool prizes to those
# guides who go above and beyond in their sales efforts. The organizers want a program
# to print the guide list and their prizes.

# Ask the user how many guides sold cookies in the current event,
# For each numbered guide up to the user-entered count of guides, allow the 
# user to enter a name and the number of boxes of cookies that person sold. 
# Calculate and output a list of all guide names, 
# Display the average sales, and the prize that each guide won,
# The highest selling guide gets a trip to the Girl Guide Jamboree, any guides
# selling above average get a badge, and any guides selling at least one box get to 
# split the remaining cookies, with guides selling no boxes shut out of all prizes 
# (as they should be).
# (Hint: Some potential solution ideas: Research parallel arrays or two-dimensional lists)

def calculation (num_of_boxes, num_of_cookies):
    average = sum(num_of_boxes)/num_of_cookies
    return average 


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Variables
    #numofcookies= 0
    name = ""
    number = 0

    num_of_cookies = int(input("Enter the number of guides selling cookies: ")) 

    name_of_guide= []
    num_of_boxes= []
    
    max_boxes = -1

    for i in range(num_of_cookies):
        name= input("Enter the name of guide #{0}: ".format(i+1))
        number= int(input("Enter the number of boxes sold by {0}: ".format(name)))
        num_of_boxes.append(number)
        name_of_guide.append(name)

        #update the maximum number of boxes
        if number > max_boxes:
            max_boxes = number

    average = calculation(num_of_boxes, num_of_cookies)
    print("The average number of boxes sold by each guide was {0:.1f}\n".format(average))
   

    print("Guide".ljust(10), "Prizes Won".rjust(20))
    print("===================================================")
    #iterate over all guides
    for k in range(num_of_cookies):
        
        #name of guide at position 'k'
        name = name_of_guide[k]
        #numOfBoxes for guide at position 'k'
        number = num_of_boxes[k]

        #check if this number is the highest number (max_boxes) 
        #if yes, print the name and respective prize (Trip to the Girl Guide Jamboree)
        if number == max_boxes:
            print(name.ljust(10), "- Trip to the Girl Guide Jamboree".rjust(20))


        #else check if this number is above average
        #if yes, print (Supper seller badge)
        elif number > average:
            print(name.ljust(10),              "- Supper seller badge".rjust(20))

        elif number >= number:
            print(name.ljust(10), "- Split leftover cookies".rjust(20))

        else:
            print(name.ljust(10), "-")

    # YOUR CODE ENDS HERE

main()