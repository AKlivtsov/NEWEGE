from turtle import *

k = 25
pensize(2)
tracer(0)
left(90)

right(30)
for _ in range(3):
    right(150)
    forward(k * 6)
    right(30)
    forward(k*12)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(2)

done() # 29
