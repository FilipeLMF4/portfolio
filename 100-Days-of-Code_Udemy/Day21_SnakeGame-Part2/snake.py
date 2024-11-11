from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
INITIAL_SPEED = 0.1
MAX_SPEED = 0.05
SPEED_UPDATE = (10, 0.01)  # (x,y) Increase speed by y every x points


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.speed = INITIAL_SPEED

    def update_speed(self):
        if (len(self.snake)-len(STARTING_POS)) % SPEED_UPDATE[0] == 0 and self.speed > MAX_SPEED:
            self.speed -= SPEED_UPDATE[1]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_segment(pos)

    def add_segment(self, pos):
        snake_seg = Turtle(shape="square")
        snake_seg.color("white")
        snake_seg.penup()
        snake_seg.goto(pos)
        self.snake.append(snake_seg)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            next_seg = self.snake[seg_num - 1].pos()
            self.snake[seg_num].goto(next_seg)

        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
