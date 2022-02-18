import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
triad = turtle.Turtle()
triad.speed(0)
triad.up()
triad.goto(0, 0)
triad.down()
colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]

for i in range(100):
    triad.color(random.choice(colors))
    triad.forward(i * 3)
    triad.left(120)
triad.up()
triad.goto(-110, 200)
triad.down()
triad.hideturtle()
turtle.done()
