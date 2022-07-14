import turtle


class ScoreBoard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Right: {self.rscore} Left: {self.lscore}", move=False, align="center",
                   font=("Arial", 12, "normal"))

    def game_over(self):
        self.goto(0, 0)
        if self.rscore == 5:
            self.write("GAME OVER, right side wins!", move=False, align="center", font=("Arial", 12, "normal"))
        else:
            self.write("GAME OVER, left side wins!", move=False, align="center", font=("Arial", 12, "normal"))

    def add_score(self, side):
        if side == self.lscore:
            self.lscore += 1
        elif side == self.rscore:
            self.rscore += 1
        self.clear()
        self.update_scoreboard()
