from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

R_PADDLE_POS = (350, 0)
L_PADDLE_POS = (-350, 0)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
left_player = screen.textinput("Left Player", "What is the name of the player on the left?").strip()
right_player = screen.textinput("Right Player", "What is the name of the player on the right?").strip()

# Screen elements
r_paddle = Paddle(R_PADDLE_POS)
l_paddle = Paddle(L_PADDLE_POS)
ball = Ball()
score = Scoreboard()

# Move paddles
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with top and bot wall
    if ball.ycor() >= SCREEN_HEIGHT/2-10 or ball.ycor() <= -SCREEN_HEIGHT/2+20:
        ball.bounce()

    # Detect collision with paddles
    if (r_paddle.ycor() - 50 < ball.ycor() < r_paddle.ycor() + 50 and
            SCREEN_WIDTH/2 - 70 < ball.xcor() < SCREEN_WIDTH/2 - 50):
        ball.hit()
        ball.increase_speed()

    if (l_paddle.ycor() - 50 < ball.ycor() < l_paddle.ycor() + 50 and
            -SCREEN_WIDTH/2 + 50 < ball.xcor() < -SCREEN_WIDTH/2 + 70):
        ball.hit()
        ball.increase_speed()

    # Detect r_paddle miss
    if ball.xcor() > SCREEN_WIDTH/2 - 20:
        ball.reset()
        score.l_point()

    # Detect l_paddle miss
    if ball.xcor() < -SCREEN_WIDTH/2 + 20:
        ball.reset()
        score.r_point()

    # Game over
    if score.l_score == score.winner:
        game_on = False
        if left_player is None or left_player == "":
            left_player = "Left Player"
        score.game_over(left_player)

    if score.r_score == score.winner:
        game_on = False
        if right_player is None or right_player == "":
            right_player = "Right Player"
        score.game_over(right_player)

screen.exitonclick()
