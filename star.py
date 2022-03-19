import random
import turtle

screen = turtle.Screen()
screen.bgcolor('black')
num = 10
turtle.speed(0)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(130):
    turtle.right(144)
    turtle.color(random.choice(colors))
    turtle.forward(num)
    num = num + 10
    turtle.pensize(2)
turtle.done()
