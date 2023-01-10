FINISH_LINE_Y = 280
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    screen.onkey(p.move, "Up")
    return screen

p = Player()
c = CarManager()
s = Scoreboard()
scr = setup_screen()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    scr.update()
    c.create_cars()
    c.move_cars()
    if p.ycor() >= FINISH_LINE_Y:
        p.nextlvl()
        c.speed_up()
        s.update()
    for car in c.cars:
        if car.distance(p) < 20:
            game_is_on = False
            s.game_over()
scr.exitonclick()