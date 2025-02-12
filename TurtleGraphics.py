#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)


def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    bob = turtle
    hideturtle()
    for i in range(5):
        forward(100)
        left(72)
    # drawPolygon(myTurtle, 8) #draws an octogon
    bob = turtle
    hideturtle()

    for i in range(8):
        forward(70)
        left(45)
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    bob = turtle
    hideturtle()
    for i in range(4):
        forward(100)
        left(90)
    
    penup()
    forward(100)
    left(90)
    forward(100)
    pendown()
    
    begin_fill()
    color("red")
    for i in range(4):
        right(-90)
        forward(50)
    end_fill()
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    bob = turtle
    hideturtle()

    for i in range(4):
        forward(100)
        left(90)

    begin_fill()
    color("red")
    for i in range(4):
        forward(50)
        left(90)
    end_fill()
    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    bob = turtle
    june = turtle
    jose = turtle
    brando = turtle
    Nena = turtle
    hideturtle()

    for Bob  in range(4):
        forward(50)
        left(90)
 
    penup()
    setposition(-8, 8)
    goto(-8, -8)
    pendown()
    for june in range(4):
        forward(62)
        left(90)

    penup()
    setposition(-12, 12)
    goto(-12, -12)
    pendown()
    for jose in range(4):
        forward(70)
        left(90)

    penup()
    setposition(-15, 15)
    goto(-15, -15)
    pendown()
    for brando in range(4):
        forward(80)
        left(90)

    penup()
    setposition(-18, 18)
    goto(-18, -18)
    pendown()
    for Nena in range(4):
        forward(92)
        left(90)
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares
    bob = turtle
    june = turtle
    jose = turtle
    brando = turtle
    Nena = turtle
    hideturtle()

    for Bob  in range(4):
        forward(50)
        left(90)
    
    penup()
    setposition(-8, 8)
    goto(-8, -8)
    pendown()
    for june in range(4):
        forward(62)
        left(90)

    penup()
    setposition(-12, 12)
    goto(-12, -12)
    pendown()
    for jose in range(4):
        forward(70)
        left(90)

main()
