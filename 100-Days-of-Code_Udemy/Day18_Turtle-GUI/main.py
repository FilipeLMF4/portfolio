###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import math
from turtle import Turtle, Screen, colormode
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)
              ]

# Hirsch Painting:
#   10 x 10 dots
#   size 20
#   spacing between each 50


def make_row(t):
    for _ in range(NR_DOTS_X):
        t.setheading(0)
        t.dot(DOT_SIZE, random.choice(color_list))
        t.pu()
        t.forward(SPACING + DOT_SIZE)
        t.pd()


def change_lane(t, y):
    t.pu()
    t.goto(FIRST_X, y)
    t.pd()


DOT_SIZE = 20
SPACING = 50
NR_DOTS_X = 10
NR_DOTS_Y = 10

if NR_DOTS_X % 2 == 0:
    FIRST_X = -((DOT_SIZE + SPACING) * (NR_DOTS_X/2 - 1) + (DOT_SIZE + SPACING) / 2)
else:
    FIRST_X = -((DOT_SIZE + SPACING) * math.floor(NR_DOTS_X / 2))

morris = Turtle()
morris.shape('turtle')
morris.speed("fastest")
morris.hideturtle()
colormode(255)

# Set first position
if NR_DOTS_Y % 2 == 0:
    y_pos = -((DOT_SIZE + SPACING) * (NR_DOTS_Y/2 - 1) + (DOT_SIZE + SPACING) / 2)
else:
    y_pos = -((DOT_SIZE + SPACING) * math.floor(NR_DOTS_Y / 2))

for _ in range(NR_DOTS_Y):
    change_lane(morris, y_pos)
    make_row(morris)
    y_pos += DOT_SIZE + SPACING

screen = Screen()
screen.exitonclick()
