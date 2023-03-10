from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15

class Player(Turtle):
    def __init__(self):
        # Configurações da tartaruga
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("turtle")
        self.color("Black")
        self.goto(STARTING_POSITION)
    def move(self):
        self.fd(MOVE_DISTANCE)
    def nextlvl(self):
        # Volta para a posição inicial
        self.goto(STARTING_POSITION)
