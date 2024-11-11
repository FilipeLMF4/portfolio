from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-230, 260)
        self.current_level = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="center", font=FONT)

    def next_level(self):
        self.current_level += 1
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
