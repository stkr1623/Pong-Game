from turtle import Turtle, Screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score =0
        self.r_score = 0

        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 260)
        self.write(self.l_score,align="center",font=("courier",30,"normal"))
        self.goto(100, 260)
        self.write(self.r_score, align="center", font=("courier", 30, "normal"))

    def l_scores(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_scores(self):
        self.r_score += 1
        self.update_scoreboard()