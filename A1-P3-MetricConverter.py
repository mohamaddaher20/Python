#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
#to the metric equivalent in metric tons, kilograms, and grams.

#After the numbers of tons, stones, pounds, and ounces are input by the user, the weight should be converted entirely into ounces 
#(the lowest common denominator) and then divided by 35.274 to obtain the value in kilos. 
# The Python int function should be used to break the total number of kilos into a whole number of metric tons and kilos.
# The number of grams should be displayed to one decimal place.

# total ounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
# total kilos = total ounces / 35.274
# metric tons = Int(kilos/1000)



def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #name for the program
    print("Imperial to Metric Conversions")
   
    #what are the inputs from the user?
    tons =(int(input("please enter the number of tons: ")))
    stones =(int(input("please enter the number of stones: ")))
    pounds =(int(input("please enter the number of pounds: ")))
    ounces =(int(input("please enter the number of ounces: ")))

    #Calculations for the given formula
    totalounces = (35840 * tons + 224 * stones + 16 * pounds + ounces)
    totalkilos = totalounces / 35.274 
    metrictons = int(totalkilos/1000)
    grams = (totalkilos % 1) * 1000
    formatted_grams = round(grams, 1)
    formatted_kilos = int(totalkilos - (metrictons * 1000))

    #output result 
    print("The metric weight is {0} metric tons, {1} kilos, and {2:.1f} grams.".format(metrictons, formatted_kilos, formatted_grams))



#The metric weight is 10 metric tons, 288 kilos, and 30.8 grams.

    # YOUR CODE ENDS HERE

main()