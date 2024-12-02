# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 10)
#
# for color in colors:
#     rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
#
#
# print(rgb_colors)
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()


color_list = [(227, 234, 242), (227, 234, 242), (245, 234, 239), (245, 234, 239), (233, 242, 236), (233, 242, 236),
              (208, 158, 96), (208, 158, 96), (234, 213, 101), (234, 213, 101), (41, 104, 144), (41, 104, 144),
              (149, 78, 57), (149, 78, 57), (130, 168, 194), (130, 168, 194), (202, 137, 162), (202, 137, 162)]

tim.setheading(225) # Turtle pointing direction
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



my_screen = t.Screen()
my_screen.screensize(100, 100)
my_screen.exitonclick()
