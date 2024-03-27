from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape, color, shapesize) -> None:
        super().__init__()
        # Params
        self.shape(shape)
        self.color(color)
        self.shapesize(shapesize)
        
        # Hard coded arguments
        self.left(90)
        self.penup()
        self.goto(STARTING_POSITION)
        
    # def move_forward(self):
    #     self.forward(MOVE_DISTANCE)
