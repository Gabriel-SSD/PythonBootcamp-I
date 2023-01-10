FINISH_LINE_Y = 280
from time import sleep
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Configura a tela, e retorna um objeto
def setup_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    screen.onkey(p.move, "Up")
    return screen

# Inicialização dos objetos
p = Player()
c = CarManager()
s = Scoreboard()
scr = setup_screen()

# Condição para o jogo continuar
game_is_on = True
while game_is_on:
    sleep(0.1)
    scr.update()
    # Cria e move os carros
    c.create_cars()
    c.move_cars()
    if p.ycor() >= FINISH_LINE_Y:
        # Quando a tartaruga chega no final
        # Aumenta a dificuldade, reinicia a posição e atualizar o score
        p.nextlvl()
        c.speed_up()
        s.update()
    for car in c.cars:
        # Verifica todos os carros por uma colisão com a tartaruga
        if car.distance(p) < 20:
            game_is_on = False
            s.game_over()
scr.exitonclick()