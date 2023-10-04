from turtle import Turtle, Screen
import random


def turtle_race(user_bet):
    is_race_on = False
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtles = []
    change_direction = 0

    for colors in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors)
        new_turtle.penup()
        y = -100 + change_direction
        new_turtle.goto(-230, y)
        change_direction += 35
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won!. the {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost!. the {winning_color} turtle is the winner!")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)


screen = Screen()
screen.setup(width=500, height=400)

to_play = screen.textinput(title="Turtle Race", prompt="Type Enter if you want to continue").capitalize()
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win race? Enter a color")
turtle_race(user_bet)

screen.exitonclick()