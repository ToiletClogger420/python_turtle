import random
import turtle

screen = turtle.Screen()
screen.bgcolor('black')
colors = ['red','orange','yellow','green','blue','purple'] # colors that the program can draw in
turtle.speed(0) # fast

def hex(size):
    turtle.forward(size)
    turtle.right(60)
num = 1
while True:
    for i in range(15):
        turtle.pencolor(random.choice(colors))
        hex(num)
        num = num + 1
        turtle.setx(-num)
    for i in range(15):
        turtle.pencolor(random.choice(colors))
        turtle.forward(-num)
        turtle.left(60)
        num = num + 1
        turtle.setx(num)
