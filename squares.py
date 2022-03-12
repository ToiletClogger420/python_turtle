import random
import turtle
# dark mode
screen = turtle.Screen()
screen.bgcolor('black')
colors = ['red','orange','yellow','green','blue','purple'] # colors that the program can draw in
turtle.speed(0) # fast

# square function
def square(size):
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
        size = size
num = 50 # size variable
# setting startpoint of the pen's drawing
turtle.setx(-900)# laptop: 763
turtle.sety(500)# laptop: 394

# drawing
while True:
    turtle.pencolor(random.choice(colors))
    square(num)
    num = num + 10
