from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

scott = Turtle()
scott.penup()
scott.goto(-400, -400)
scott.write('Etch A Sketch - Use your arrow keys to move. Press c to clear.', font=('Courier', 20, 'bold'))
scott.hideturtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
