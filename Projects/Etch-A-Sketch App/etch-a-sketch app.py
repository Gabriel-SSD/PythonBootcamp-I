# Imports
from turtle import Turtle, Screen

# Functions
def movefd ():
    turtle.forward(20)
def movebck ():
    turtle.backward(20)
def movelft ():
    turtle.left(30)
def moveright():
    turtle.right(30)
def clear ():
    turtle.reset()

turtle = Turtle()
screen = Screen()
screen.listen()
screen.onkey(key="w", fun=movefd)
screen.onkey(key="a", fun=movelft)
screen.onkey(key="s", fun=movebck)
screen.onkey(key="d", fun=moveright)
screen.onkey(key="c", fun=clear)

screen.exitonclick()