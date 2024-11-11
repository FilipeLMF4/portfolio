from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.refresh_score()

    def refresh_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)
        self.goto(0, -15)
        self.write(arg="Click on screen to exit", move=False, align=ALIGNMENT, font=("Arial", 8, "normal"))
