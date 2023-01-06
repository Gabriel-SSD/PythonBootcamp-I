from turtle import Turtle
ALIGN = "center"
FONT =  ('Courier', 50, 'normal')
class Scoreboard(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(x, 200)
        self.write(self.score, align=ALIGN, font=FONT)
    def update(self):
        self.score += 1
        self.clear()
        self.write(self.score, align=ALIGN, font=FONT)
