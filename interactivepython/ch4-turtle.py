import turtle
import random
import time
import os

window = turtle.Screen()
canvas = window.getcanvas()

print(canvas)

bip = turtle.Turtle()
bop = turtle.Turtle()


angles = [90, 90, 90, 90, 90, 90, 90, 30, 45, 27, 191]
# angles = [0, 30, 60, 30, 60, 23]


mod = 3
positions = []

def draw_rectangle(turtle, side1, side2, c=1):
    width = 2 * random.random()
    turtle.width(width)
    for i in range(2):
        turtle.forward(side1)
        turtle.left(90 * c)
        turtle.forward(side2)
        turtle.left(90 * c)

def draw_triangle(turtle, side_length):
    width = random.random()
    turtle.width(width)
    for i in range(3):
        turtle.forward(side_length)
        if width > .5:
            turtle.left(-120)
        else:
            turtle.left(120)
    turtle.forward(side_length)


def to_location_and_back(turtle, location=(0, 0), width=.25):
    turtle.width(width)
    position = turtle.position()
    turtle.setposition(location)
    turtle.penup()
    turtle.setposition(position)
    turtle.pendown()

for i in range(40):


    dist = random.randint(50, 90)
    idx = random.randint(0, len(angles)-1)

    bip.penup()

    bip.forward(dist)
    bop.backward(dist)
    bip.left(angles[idx])
    bop.right(angles[idx])
    bop.dot(dist / 6)
    bop.width(.25)

    bip.pendown()

    draw_rectangle(bip, random.randint(10, 50), 5)
    draw_rectangle(bip, 5, random.randint(10, 100), c=-1)
    draw_triangle(bip, random.randint(20, 30))
    # to_location_and_back(bip)


    if i % 2 == 0:
        bip.pendown()
        bip.circle(dist / 7)
        bip.penup()
    else:
        bip.dot(dist / 5)

path = '/home/tyler/Dropbox/Turtle/{}'.format(time.strftime('%Y-%m-%d'))

if not os.path.exists(path):
    os.mkdir(path)

bip.ht()
ps = canvas.postscript(file=path + "/turtle_{}.ps".format(time.strftime("%Y-%m-%d_%H%M%S")))

print(ps)

window.exitonclick()
