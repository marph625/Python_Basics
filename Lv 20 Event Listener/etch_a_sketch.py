from turtle import Turtle, Screen

little_dude = Turtle()
screen = Screen()

little_dude.shape("turtle")
little_dude.color("green")
little_dude.shapesize(3)

def mv_fd():
    little_dude.fd(20)
    
def mv_bd():
    little_dude.bk(20)
    
def turn_left():
    little_dude.left(90)
    
def turn_right():
    little_dude.right(90)
    
def pen_up():
    little_dude.pu()
    
def pen_down():
    little_dude.pd()

def clear_screen():
    little_dude.clear()
    little_dude.pu()
    little_dude.home()
    little_dude.pd()

screen.listen()

screen.onkey(mv_fd, "w")
screen.onkey(mv_bd, "s")
screen.onkey(turn_left, "a")
screen.onkey(fun=turn_right, key="d")
screen.onkey(pen_up, "q")
screen.onkey(pen_down, "e")
screen.onkey(clear_screen, "space")

screen.exitonclick()