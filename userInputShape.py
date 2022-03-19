import turtle

num = 360
print("this is a program that makes shapes based on how many sides you input")
side_num = input("how many sides do you want your shape to have")
side_num = int(side_num)
shape_angle = num / side_num

for i in range(side_num):
    turtle.forward(50)
    turtle.right(shape_angle)
turtle.done()
