# Imports
from turtle import Turtle, Screen, colormode
from random import choice
from cores import cores

# Configurações Iniciais
colormode(255)  # Permite utilizar cores rgb
turtle = Turtle()
turtle.penup()  # Não permite a tartaruga desenhar
turtle.hideturtle() # Esconde a tartaruga
turtle.speed("fastest")
def drawdots():
    # Desenha 10 pontos em cada linha, em 10 linhas diferentes
    tpos = (-200, 0)
    for b in range(1, 11):
        turtle.goto(tpos)
        turtle.sety(b * 50)
        for a in range(1, 11):
            turtle.dot(20, choice(cores))
            turtle.fd(50)
drawdots()
screen = Screen()
screen.exitonclick()