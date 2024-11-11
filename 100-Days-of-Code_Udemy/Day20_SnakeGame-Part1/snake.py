from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for pos in STARTING_POS:
            snake_seg = Turtle(shape="square")
            snake_seg.color("white")
            snake_seg.penup()
            snake_seg.goto(pos)
            self.snake.append(snake_seg)

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
