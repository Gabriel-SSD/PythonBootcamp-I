# Arquivo de teste da biblioteca turtle

from turtle import Turtle, Screen, colormode
from random import choice, randint

colormode(255)
turtle = Turtle()
turtle.shape("turtle")

def randomcolor ():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    tup = (r, g, b)
    return tup

def spirograph ():
    turtle.hideturtle()
    turtle.speed("fastest")
    for l in range(72):
        turtle.color(randomcolor())
        turtle.circle(1000)
        turtle.right(5)
def drawshape(vertices):
    turtle.color(randomcolor())
    for _ in range(vertices):
        turtle.right(360/vertices)
        turtle.forward(100)

def randomwalk():
    directions = [0, 90, 180, 270]
    for _ in range(100):
        dire = choice(directions)
        turtle.color(randomcolor())
        turtle.forward(20)
        turtle.setheading(dire)
for i in range(3, 10):
    drawshape(i)
randomwalk()
spirograph()
screen = Screen()
screen.exitonclick()