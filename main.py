import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_positions = [-80, -40, 0, 40, 80, 120]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed(6)
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            winn = turtle.home()
            if winning_color == user_bet:
                print(f"You've win {winning_color} {winn}turtle is the winner")
            else:
                print(f"You've lost The {winning_color} {winn} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()