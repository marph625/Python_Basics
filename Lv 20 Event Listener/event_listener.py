from turtle import Turtle, Screen

myturtle = Turtle()
screen = Screen()

def move_forward():
    myturtle.fd(10)
    
def turn_left():
    myturtle.left(90)
    
def turn_right():
    myturtle.right(90)

"""
+================================+
|                                |
|      Lv 20 Eventlistener       |
|     Higher Order Functions     |
+================================+
"""

# Eine Funktion die mit anderen Funktionen als Parameter arbeitet, wird
# als Higher Order Function bzw. Funktion höherer Ordnung bezeichnet

screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.exitonclick()