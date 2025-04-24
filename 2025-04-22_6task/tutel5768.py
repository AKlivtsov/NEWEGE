from turtle import *

k = 15
pensize(3)
left(90)
tracer(0)

for _ in range(3):
    forward(10 * k)
    right(120)

penup()

forward(10 * k)
right(90)
forward(3 * k)

pendown()
for _ in range(4):
    forward(10 * k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3)

done()  # 13
