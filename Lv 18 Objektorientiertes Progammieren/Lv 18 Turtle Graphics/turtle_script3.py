from turtle import Turtle
from random import random

t = Turtle()
for i in range(20):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()