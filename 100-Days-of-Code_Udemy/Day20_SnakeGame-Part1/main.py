from turtle import Turtle, Screen
import time
from snake import Snake

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)  # Turn animation off

# Initialize Snake and movement
snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)  # Snake speed

    snake.move()

screen.exitonclick()
