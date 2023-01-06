from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()

    def create_paddle(self, x):
        self.penup()
        self.color("White")
        self.shape("square")
        self.turtlesize(1, 5, 1)
        self.right(90)
        self.goto(x=x, y=15)

    def up(self):
        self.bk(40)
    def down(self):
        self.fd(40)
