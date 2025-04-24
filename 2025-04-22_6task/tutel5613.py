from turtle import *

k = 15
pensize(3)
left(90)
tracer(0)

for _ in range(12):
    forward(210)
    right(216)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(3)

done()  # 15
