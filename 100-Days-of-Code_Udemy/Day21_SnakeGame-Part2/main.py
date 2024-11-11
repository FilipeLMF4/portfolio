from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0)  # Turn animation off

# Limits of playable zone
# from turtle import Turtle
# limits = Turtle()
# limits.penup()
# limits.color("red")
# limits.speed("fastest")
# limits.goto(-290, -290)
# limits.pendown()
# limits.setheading(90)
# limits.goto(-290, 280)
# limits.setheading(0)
# limits.goto(290, 280)
# limits.setheading(270)
# limits.goto(290, -290)
# limits.setheading(180)
# limits.goto(-290, -290)
# limits.hideturtle()

# Initialize Snake and movement
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Start game
game_on = True
while game_on:
    screen.update()
    time.sleep(snake.speed)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()
        snake.update_speed()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()


screen.exitonclick()
