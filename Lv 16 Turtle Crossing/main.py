import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
#screen.tracer(0)



p1 = Player("turtle", "green")

def mv_fd():
    p1.fd(20)

def mv_bk():
    p1.bk(20)

def turn_left():
    p1.left(90)

def turn_right():
    p1.right(90)

screen.listen()

screen.onkey(fun=mv_fd, key="e")
# screen.onkey(fun=mv_bk, key="d")
# screen.onkey(fun=turn_left, key="s")
# screen.onkey(fun=turn_right, key="f")

# game_is_on = True
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()

#Screen.clearscreen()
screen.exitonclick()