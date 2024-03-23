from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape, color) -> None:
        super().__init__(shape, color)
        #self.goto(STARTING_POSITION)
