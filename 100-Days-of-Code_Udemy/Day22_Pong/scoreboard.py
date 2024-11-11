from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
MAX_SCORE = 5


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.winner = MAX_SCORE
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.goto(0, 250)
        self.write(f"First to {self.winner}", align=ALIGNMENT, font=("Courier", 12, "normal"))

    def r_point(self):
        self.r_score += 1
        self.write_score()

    def l_point(self):
        self.l_score += 1
        self.write_score()

    def game_over(self, player):
        self.write_score()
        self.goto(0, 0)
        self.write(f"Game Over. {player} wins!", align=ALIGNMENT, font=("Courier", 20, "normal"))
        self.goto(0, -20)
        self.write("Click on screen to exit", align=ALIGNMENT, font=("Courier", 12, "normal"))
