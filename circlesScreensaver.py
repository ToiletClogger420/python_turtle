import random
import turtle

bg = turtle.Screen()
# dark mode
bg.bgcolor('black')
# colors that the pen will draw in
colors = ['red','orange','yellow','green','blue','purple']
# making pen fast
turtle.speed(0)
# setting the location of the pen
turtle.setx(100)
turtle.sety(240)
# loop that does the drawing
while True:
    for i in range(8):
        for i in range(21):
            turtle.pencolor(random.choice(colors))
            turtle.circle(100)
            turtle.left(15)
        turtle.forward(200)
    turtle.clear()
