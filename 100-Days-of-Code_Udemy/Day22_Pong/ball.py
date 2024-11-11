from turtle import Turtle

BALL_MOVEMENT = 10
INITIAL_BALL_SPEED = 0.1


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = BALL_MOVEMENT
        self.y_move = BALL_MOVEMENT
        self.ball_speed = INITIAL_BALL_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.ball_speed = INITIAL_BALL_SPEED
        self.hit()

    def increase_speed(self):
        self.ball_speed *= 0.9
