import turtle
from random import randint

myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(500)
myPen.pensize(2)
turtle.colormode(255)
#draw snowflake
def snowflake(color,x,y,size,branches):
    # -> object:
    """
    :rtype: object
    """
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    myPen.left(90)
    # draw Branches
    for i in range(0, branches):
        myPen.forward(100 * size/100)
        myPen.forward(-40 * size/100)
        myPen.left(40)
        myPen.forward(30* size/100)
        myPen.forward(-30* size/100)
        myPen.right(80)
        myPen.forward(30* size/100)
        myPen.forward(-30* size/100)
        myPen.left(40)
        myPen.forward(-60* size/100)
        myPen.right(360/branches)
    #return myPen #turtle.exitonclick()
#greetings
def addText(message, color, x, y, size,tfmt):
    myPen.penup()
    myPen.goto(x, y)
    myPen.pendown()
    myPen.color(color)
    style = ('Courier', size, tfmt)
    myPen.write(message, font=style, align='center')

#generate snowflake
def rand_snow():
    for i in range(0,20):
        randomX = randint(-180,180)
        randomY = randint(-180,180)
        randomSize = randint(5,40)
        redA = randint(0,255)
        greenA = randint(0,255)
        blueA = randint(0,255)
        random_color = (redA,greenA,blueA)
        branches = randint(5,10)
        snowflake(random_color,randomX,randomY,randomSize,branches)
addText('Let it snow challenge','pink',0,0,30,'italic')
addText('Have a great day','red',0,-30,15,'bold')