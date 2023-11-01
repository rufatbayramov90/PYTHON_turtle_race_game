from turtle import Turtle, Screen


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

tim = Turtle(shape="turtle")
tim.speed(1)
tim.penup()
tim.goto(x=-220, y=-100)


screen.exitonclick()