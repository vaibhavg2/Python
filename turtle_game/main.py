import turtle
from turtle import Turtle,Screen
import random

screen = Screen()

race_start=False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
position = -100
turtles = []

for color in colors:
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-230, position)
    position += 30
    turtles.append(new_turtle)

if user_bet:
    race_start = True

while race_start:
    for tim in turtles:
        if tim.xcor() > 230:
            race_start = False
            winning_color = (tim.pencolor()).lower()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is winner!")

        distance = random.randint(0, 10)
        tim.forward(distance)
screen.exitonclick()
