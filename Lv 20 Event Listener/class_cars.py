from turtle import Turtle
from colorlist import color_list
import random

class Turtle():
    def __init__(self):
        self.color = "green"
        self.shapesize = 3
        self.shape = "turtle"

class Car(Turtle):
    def __init__(self):
        super().__init__(self, shapesize)
        self.color = random.choice(color_list)
        self.shape = "square"

