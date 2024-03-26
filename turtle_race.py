from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color:\n(red, orange,yellow,green,blue,purple)").lower()
print(user_bet)
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
x = -230
y = 150
game_on = True
tim = Turtle()
tim.penup()
tim.hideturtle()
tim.goto(-150, 0)


class TurtleRace:

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color_list[turtle_index])
        new_turtle.penup()
        turtle_list.append(new_turtle)
        new_turtle.goto(x=x, y=y)
        y -= 50

    if user_bet:
        game_on = True

    while game_on:
        for turtle in turtle_list:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    tim.write(f"You've won! The {winning_color} turtle is the winner.", move=False, align="left", font=("Arial", 12, "normal"))
                else:
                    tim.write(f"You've lost! The {winning_color} turtle is the winner.", move=False, align="left", font=("Arial", 12, "normal"))
                game_on = False

            random_length = random.randint(1, 10)
            random_speed = random.randint(1, 10)
            turtle.speed(random_speed)
            turtle.forward(random_length)

    screen.exitonclick()
