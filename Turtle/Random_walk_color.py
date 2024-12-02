import turtle
from turtle import Turtle, Screen
import random

# object = class()
timmy = Turtle()

""" Random walk and color"""
# colors = ["MediumBlue", "Sienna", "Chartreuse", "SeaGreen", "Maroon", "DarkOrchid",
#           "CadetBlue", "Gold", "BlueViolet", "MediumPurple"]
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r, g, b)
    return random_colors


directions = [0, 90, 180, 270]
for _ in range(200):
    timmy.setheading(random.choice(directions))
    timmy.color(random_color())
    timmy.forward(30)
    timmy.pensize(15)
    # fastest, fast,normal, slow, slowest
    timmy.speed("fastest")

my_screen = Screen()
print(my_screen.canvwidth, my_screen.canvheight)
my_screen.exitonclick()
