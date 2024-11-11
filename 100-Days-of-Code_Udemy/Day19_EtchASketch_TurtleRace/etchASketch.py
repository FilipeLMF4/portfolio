from turtle import Turtle, Screen

mariza = Turtle()
screen = Screen()


def move_forwards():
    mariza.forward(10)


def move_backwards():
    mariza.backward(10)


def turn_right():
    current_head = mariza.heading()
    mariza.setheading(current_head+10)


def turn_left():
    current_head = mariza.heading()
    mariza.setheading(current_head-10)


def clear_screen():
    mariza.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_right)
screen.onkey(key="d", fun=turn_left)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()