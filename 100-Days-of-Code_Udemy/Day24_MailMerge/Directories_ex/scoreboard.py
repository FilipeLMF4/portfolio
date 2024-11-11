from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(0, 280)
        self.refresh_score()

    def refresh_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score} | High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.refresh_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.highscore))

        self.score = 0
        self.refresh_score()
