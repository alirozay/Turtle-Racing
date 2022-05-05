from turtle import Turtle, Screen
import random
is_race_on = False
x_cord = -240
y_cord = -180
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
shape = "turtle"
red, orange, yellow, green, blue, purple = \
    Turtle(shape), Turtle(shape), Turtle(shape), Turtle(shape), \
              Turtle(shape), Turtle(shape)
turtles = [red, orange, yellow, green, blue, purple]
for i in range(len(turtles)):
    turtles[i].pu()
    turtles[i].color(colors[i])
    turtles[i].goto(x=x_cord, y=y_cord)
    y_cord += 50


screen = Screen()
user_prompt = screen.textinput(title="Make a bet",
                               prompt="Which color is going to win the race?: ")

if user_prompt:
    is_race_on = True
while is_race_on:

    for i in range(len(turtles)):
        if turtles[i].xcor() > (screen.window_width()/2) - (turtles[i].shapesize()[0]/2):
            is_race_on = False
            if turtles[i].pencolor() == user_prompt:
                print(f"You have won! The winning color was {turtles[i].pencolor()}.")
            else:
                print(f"You lost. The winning color was {turtles[i].pencolor()}.")
            break
        else:
            random_distance = random.randint(0,10)
            turtles[i].forward(random_distance)
screen.screensize(canvwidth=500, canvheight=400)
screen.bye()
