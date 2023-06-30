import random
from turtle import Turtle, Screen

tim = Turtle()

# tim.shape('turtle')
# tim.color("orange")
# n=4
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     n -=1
# import heroes
#
# screen=Screen()
# screen.exitonclick()

# Pentagon

# num_side = 360
#
#
# def drew_shape(num_side):
#     for _ in range(num_side):
#         angle = 360 / num_side
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     drew_shape(shape_side_n)


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)


colours = ['GreenYellow', 'OrangeRed', 'SlateBlue', 'medium blue', 'Goldenrod', 'SkyBlue']
directions = [0, 90, 180, 270]
tim.pensize(3)
tim.speed('fastest')

for _ in range(20):
    tim.color(random_color())
    # tim.forward(30)
    # tim.setheading(random.choice(directions))
    tim.circle(100)
    current_heading = tim.heading()
    tim.setheading(current_heading +10)
screen = Screen()
screen.exitonclick()