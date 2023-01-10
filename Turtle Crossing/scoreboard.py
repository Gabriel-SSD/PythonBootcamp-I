from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Level {self.score}", align=ALIGN , font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Level {self.score}", align=ALIGN , font=FONT)

