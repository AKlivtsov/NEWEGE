from turtle import *

tracer(0)
pensize(2)
k = 15
left(90)

for _ in range(2):
    fd(27*k)
    right(90)
    fd(8*k)
    right(90)

penup()
fd(4*k)
right(90)
fd(2*k)
left(90)

pendown()
for _ in range(2):
    fd(17*k)
    right(90)
    fd(7*k)
    right(90)

penup()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k, y*k)
        dot(5)

done() # 270