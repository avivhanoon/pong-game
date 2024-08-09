from turtle import Turtle
ALIGN = "center"
FONT = ("courier", 80, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_right = 0
        self.score_left = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_left, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.score_right, align=ALIGN, font=FONT)
    def left_point(self):
        self.score_left += 1
        self.clear()
        self.update_scoreboard()
    def right_point(self):
        self.score_right += 1
        self.clear()
        self.update_scoreboard()

