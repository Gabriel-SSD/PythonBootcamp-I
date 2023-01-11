from turtle import Turtle
ALIGN = "center"
FONT =  ('Courier', 18, 'normal')
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 240)
        self.score = 0
        with open("highscore.txt", "r") as file:
            self.highscore = int(file.read())
        self.write(f"Score: {self.score}\nHighscore: {self.highscore}", align=ALIGN , font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        if self.score > self.highscore:
            with open("highscore.txt", "w") as file:
                file.write(f"{self.score}")

    def update(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}\nHighscore: {self.highscore}", align=ALIGN , font=FONT)