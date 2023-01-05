from turtle import Turtle
from random import choice

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.locals = []
        for i in range(-280, 281, 20):
            self.locals.append(i)
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        x = choice(self.locals)
        y = choice(self.locals)
        self.goto(x, y)