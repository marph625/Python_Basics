from turtle import Turtle, Screen
import random

# OBJECTS
little_dude = Turtle()
car = Turtle()
screen = Screen()

# SCREEN
screen.bgcolor("yellow")
screen.title("Tina the Turtle")

# PLAYER
little_dude.shape("turtle")
little_dude.color("green")
little_dude.shapesize(3)
little_dude.pensize(10)
little_dude.pencolor('#3D2B1F')
little_dude.pu()
little_dude.setposition(0, -400)
little_dude.left(90)

# CAR
color_list = ["aquamarine", "aquamarine4", "bisque4", "blue", "BlueViolet", "brown1", "CadetBlue1", "chartreuse", "chartreuse4", "chocolate", "coral2",
            "DarkOliveGreen3", "DarkGoldenrod1", "DarkGreen", "DarkOrange1", "DarkRed", "DarkSeaGreen3", "DarkSlateGray", "DeepPink2", "DarkTurquoise", "DeepSkyBlue"]
car.shape("square")
car.color(color_list[3])
car.shapesize(3)
car.pu()
car.setposition(0, 400)

def mv_fd():
    little_dude.fd(200)
    
def mv_bd():
    little_dude.bk(20)
    
def turn_left():
    little_dude.left(10)
    
def turn_right():
    little_dude.right(10)
    
def pen_up():
    little_dude.pu()
    
def pen_down():
    little_dude.pd()

def clear_screen():
    # player position reset
    little_dude.clear()
    little_dude.pu()
    little_dude.home()
    little_dude.left(90)
    little_dude.setposition(0, -400)

    # car position reset
    car.clear()
    car.pu()
    car.home()
    car.setposition(0, 400)

screen.listen()

screen.onkey(mv_fd, "w")
screen.onkey(mv_bd, "s")
screen.onkey(turn_left, "a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(pen_up, "q")
screen.onkey(pen_down, "e")
screen.onkey(clear_screen, "space")

screen.exitonclick()