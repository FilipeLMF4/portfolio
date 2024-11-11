from turtle import Turtle, Screen

mariza = Turtle()
screen = Screen()

def move_forwards():
    mariza.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()