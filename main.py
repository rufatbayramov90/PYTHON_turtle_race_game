from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "blue", "green", "yellow", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.speed(1)
    tim.penup()
    tim.goto(x=-220, y=y_positions[turtle_index])


screen.exitonclick()