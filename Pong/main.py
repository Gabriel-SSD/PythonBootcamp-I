from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Scoreboard
def setup_screen():
    # Configura a tela, escuta as teclas e retorna um obj
    scr = Screen()
    scr.tracer(0)
    scr.setup(width=800, height=600)
    scr.bgcolor("black")
    scr.title("Pong")
    scr.listen()
    scr.onkey(paddler.down, "Down")
    scr.onkey(paddler.up, "Up")
    scr.onkey(paddlel.down, "s")
    scr.onkey(paddlel.up, "w")
    return scr

# Inicializa os objetos
paddlel = Paddle();paddlel.create_paddle(x=-350)
paddler = Paddle();paddler.create_paddle(x=350)
scorel = Scoreboard(-100)
scorer = Scoreboard(100)
ball = Ball()
screen = setup_screen()


is_on = True
# Loop principal, ativo até algum jogador alcançar 10 pontos
while is_on:
    sleep(ball.move_speed)      # Velocidade da bola
    screen.update()             # Atualiza a tela
    ball.move()                 # Movimentação da bola
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Verifica se a bola bateu no teto, e rebate
        ball.bounce_y()
    if ball.distance(paddler) < 50 and ball.xcor() > 325 or ball.distance(paddlel) < 50 and ball.xcor() < -325:
        # Verifica se a bola bateu no paddle, e rebate
        ball.bounce_x()
    elif ball.xcor()>350:
        # Verifica se a bola passou, incrementa ponto e recomeça
        ball.restart(-10)
        scorel.update()
    elif ball.xcor()<-350:
        # Verifica se a bola passou, incrementa ponto e recomeça
        ball.restart(10)
        scorer.update()
    elif scorer.score == 10:
        print("Player 2 wins!")
        is_on = False
    elif scorel.score == 10:
        print("Player 1 wins!")
        is_on = False
