from turtle import Turtle, Screen
import random


def set_lines():
    line_marker = Turtle()
    line_marker.speed("fastest")
    line_marker.hideturtle()

    # Starting Line
    line_marker.penup()
    line_marker.goto(-230+20, 90)
    line_marker.setheading(270)
    line_marker.pendown()
    line_marker.goto(-230+20, -80)

    # Finish Line
    line_marker.penup()
    line_marker.goto(230, 90)
    line_marker.setheading(270)
    line_marker.pendown()
    line_marker.goto(230, -80)


race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "black", "green", "blue", "purple"]

turtles = []
start_y = -70

set_lines()

for color in colors:
    turtle_i = Turtle(shape="turtle")
    turtle_i.color(color)
    turtle_i.penup()
    turtle_i.goto(x=-230, y=start_y)
    start_y += 30
    turtles.append(turtle_i)

if user_bet:
    race_on = True

# Turtle bounding box is a 40x40 square
while race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:  # 250-(40/2)
            race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"You lost! The {winning_turtle} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()