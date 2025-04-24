from turtle import *

k = 15
pensize(3)
left(90)
tracer(0)

for _ in range(3):
    forward(27 * k)
    right(90)
    forward(12 * k)
    right(90)

penup()

forward(4 * k)
right(90)
forward(6 * k)
left(90)

pendown()
for _ in range(3):
    forward(83 * k)
    right(90)
    forward(77 * k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3)

done()  # 168
