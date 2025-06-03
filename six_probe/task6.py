from turtle import *

k = 30
pensize(2)
left(90)
tracer(0)

for _ in range(4):
    forward(5*k)
    right(90)
    forward(7*k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(5)

done()

# 48