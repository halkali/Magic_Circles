import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)
def colorm():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

timmy = Turtle()
timmy.speed("fastest")
for a in range(0, 360, 3):
    timmy.circle(100)
    timmy.setheading(a)
    timmy.color(colorm())













screen = Screen()
screen.exitonclick()