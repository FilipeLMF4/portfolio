import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Setup objects
morris = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(morris.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    # Detect Collision
    for car in cars.all_cars:
        if car.ycor() - 25 < morris.ycor() < car.ycor() + 15 and morris.distance(car) < 25:
            game_is_on = False
            score.game_over()

    # Next Level
    if morris.check_finish():
        score.next_level()
        morris.start_over()
        cars.increase_speed()

screen.exitonclick()
