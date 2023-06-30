from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

    def score_increase(self):
        self.score += 1
        print(self.score)
        self.display_score(self.score)

    def display_score(self, score):
        self.color("white")
        self.hideturtle()
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.write(f"Your score is {score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", move=False, align=ALIGNMENT, font=FONT)