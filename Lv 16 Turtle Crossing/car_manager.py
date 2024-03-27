from player import Player
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Player):
    def __init__(self, shapesize):
        super().__init__("square", random.choice(COLORS), shapesize)
        self.penup()
        self.setposition(0, 400)


    def move(self):
        self.forward(MOVE_INCREMENT)

