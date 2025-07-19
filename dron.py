from turtle import *

t1 = Turtle()
t1.shapesize(4)
speed = 100


while True:
    Command = input()
    if Command == 'f':
        t1.forward(speed)
    elif Command == 'l':
        t1.left(90)
    elif Command == '+':
        speed = speed+50
    elif Command == '-':
        speed = speed-50
    elif Command == 'r':
        t1.right(90)
    elif Command == 'exit':
        exit()
    elif Command == 'rg':
        t1.right(45)
    elif Command == 'lg':
        t1.left(45)
