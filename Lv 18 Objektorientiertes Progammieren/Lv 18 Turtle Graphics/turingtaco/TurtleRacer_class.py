import turtle
import random

class TurtleRacer:
    def __init__(self, color, position):
        self.turtle = turtle.Turtle(shape="turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.setposition(position)

    def race(self):
        distance = random.randint(1, 10)
        self.turtle.forward(distance)

class FastTurtleRacer(TurtleRacer):
    def __init__(self, color, position, speed):
        super().__init__(color, position)
        self.speed = speed

    def turboboost(self):
        self.speed += 5

    def race(self):
        self.turtle.pendown()
        self.turtle.forward(self.speed)