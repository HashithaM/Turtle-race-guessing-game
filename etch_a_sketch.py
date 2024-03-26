from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
tim.speed("fastest")


def turn_right():
    tim.setheading(tim.heading() - 10)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() + 10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


class EtchASketch:

    screen.listen()
    screen.onkey(key="Up", fun=move_forward)
    screen.onkey(key="Down", fun=move_backward)
    screen.onkey(key="Left", fun=turn_left)
    screen.onkey(key="Right", fun=turn_right)
    screen.onkey(key="c", fun=clear)
    screen.exitonclick()
