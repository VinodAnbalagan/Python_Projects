from turtle import Turtle, Screen
import random

# object = class()
timmy = Turtle()
timmy.shape("turtle")


"""Square"""
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)

"""Dotted lines"""
# for _ in range(4):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

""" Draw a triangle, square, pentagon, hexagon
 octagon, nonagon and decagon."""

colors = ["CornflowerBlue", "DarkOrchid", "Firebrick", "Goldenrod", "LightCoral"
                                                                    "LightSeaGreen", "MediumOrchid", "MediumPurple",
          "MistyRose", "Plum"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        timmy.forward(100)
        timmy.right(angle)


for shape_side_n in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)

my_screen = Screen()
print(my_screen.canvwidth, my_screen.canvheight)
my_screen.exitonclick()
