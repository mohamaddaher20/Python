# Random Metric Number 

# 5 by 5 grid random numbers. Store in a 2d list. Print to screen in a 5 x 5
# grid layout. With the list name matrix = []
# 1 2 3 4 5 
# 6 7 8 9 0
# 2 4 5 7 8

import random

matrix = []
gridsize = 5
for rowIndex in range(gridsize):
    templist = []
    for colIndex in range(gridsize):
        number = random.randint(1,100)
        templist.append(number)
    matrix.append(templist)

for rowIndex in range (len(matrix)):
    for colIndex in range(len(matrix)):
        print(matrix[rowIndex][colIndex], end=" ")
    print()



