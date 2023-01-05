# Imports
from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

def setup_screen():
    # Screen configs
    scr = Screen()
    scr.tracer(0)
    scr.setup(width=600, height=600)
    scr.bgcolor("black")
    scr.title("My Snake Game")
    return scr

def end_game():
    # Print game over and end the game
    scoreboard.game_over()
    return False

# Start of main
screen = setup_screen()
snake = Snake() # Create 3 segments of snake
food = Food()   # Create food on random pos [280, -280]
scoreboard = Scoreboard()   # Create the scoreboard

# Listen to keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_on = True    # Condidition

while is_on:
    sleep(0.1)
    screen.update()
    snake.move()

    # When the snake eats
    if snake.head.distance(food) < 15:
        food.refresh()  # New location
        snake.extend()  # Grow up
        scoreboard.update() # Update the scoreboard

    # When the snake hit a wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_on = end_game()

    # Look for snake hitting own tail
    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            is_on = end_game()
screen.exitonclick()