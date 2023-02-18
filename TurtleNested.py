

import turtle, random

#Custom function for turning the lines random colors
#Uses a list of colors and grabs a random index value
def GetRandomColor():
    listOfColors = ["red", "blue", "green", "pink", "purple", "orange", "black", "cyan", "magenta"]
    return listOfColors[random.randint(0, len(listOfColors) - 1)]


bob = turtle.Turtle()

bob.speed(1)
bob.pensize(1)
bob.shape("turtle")

bob.penup()
bob.goto(-100, 100)  # Where to start
bob.pendown()
bob.pencolor()
#Set Variables
length = 200 #Set the length to number and then divide it by half
numofsides = int(input("How many sides do you want"))
DEGREES_IN_A_CIRCLE = 360
angle = DEGREES_IN_A_CIRCLE / numofsides

for i in range(numofsides):  # Use for loop instead of repeating them.
    bob.forward(length)    # Draw a line, Use variables becasue we are dividing every length by 2
    bob.right(angle)
    for j in range(numofsides):
        bob.forward(length / 2)
        bob.right(angle)
        for k in range(numofsides):
            bob.forward(length / 4)
            bob.right(angle)
            for l in range(numofsides):
                bob.forward(length / 8)
                bob.right(angle)


turtle.done()