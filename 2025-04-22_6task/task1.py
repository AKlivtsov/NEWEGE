from turtle import *

tracer(0)
left(90)
pensize(3)

k = 15
for _ in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)

penup()
forward(k)
right(90)
forward(5 * k)
left(90)
pendown()

for _ in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(5)

done()
