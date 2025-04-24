from turtle import *

k = 15
tracer(0)
pensize(3)
left(90)

for _ in range(2):
    forward(23 * k)
    right(90)
    forward(10*k)
    right(90)

forward(3*k)
left(90)
forward(12*k)
right(90)

for _ in range(2):
    forward(9 * k)
    right(90)
    forward(32 * k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(3)

done()