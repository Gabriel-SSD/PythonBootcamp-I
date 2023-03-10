from turtle import Turtle
from random import choice, randint
STARTING_X = 280
STARTING_Y = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager:
    def __init__(self):
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
    def create_cars(self):
        # Gera um número aleatório para ser a frequência da criação de carros
        random_num = randint(1, 4)
        if random_num == 1:
            # Cria um carro, com o Y aleatório, e adiciona o carro na lista de todos os carros
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_len=3, stretch_wid=1)
            new_car.goto(STARTING_X, choice(STARTING_Y))
            self.cars.append(new_car)
    def move_cars(self):
        # Percorre toda a lista de carros, e os move
        for f in self.cars:
            f.bk(self.speed)
    def speed_up(self):
        # Aumenta a velocidade
        self.speed += MOVE_INCREMENT