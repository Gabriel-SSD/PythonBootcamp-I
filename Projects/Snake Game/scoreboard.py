from turtle import Turtle
ALIGN = "center"
FONT =  ('Courier', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score: {self.score}", align=ALIGN , font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN , font=FONT)