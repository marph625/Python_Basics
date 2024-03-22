from turtle import Turtle, Screen
from colorlist import color_list
import random

myDudu = Turtle()
screen = Screen()

myDudu.shape("turtle")
myDudu.color("green")
screen.bgcolor("black")
screen.title("Freddy the Turtle")

# Bereich für Lösungen

""" myDudu.forward(100)
myDudu.left(90)
myDudu.forward(100)
myDudu.left(90)
myDudu.forward(100)
myDudu.left(90)
myDudu.forward(100) """

# Formt mit der Turtle ein Quadrat

""" for x in range(4):
    myDudu.forward(200)
    if x == 3:
        break
    myDudu.left(90) """

# Mit der Turtle eine gestrichelte Linie zeichnen

# Mit Shift+Alt+A markierten Text mehrzeilig auskommentieren und rückgängig machen
# Mit STRG+k + STRG+c markierten Text einzeilig auskommentieren
# Mit STRG+k + STRG+u oberen Schritt rückgängig machen

# """ myDudu.fd(20)
# myDudu.penup()
# myDudu.fd(20)
# myDudu.pendown()
# myDudu.fd(20) """

# Mit der Turtle ein gestricheltes Quadrat zeichnen

""" for i in range(4):
    for _ in range(4):
        myDudu.fd(20)
        myDudu.up()
        myDudu.fd(20)
        myDudu.down()
    if i == 3:
        break
    myDudu.left(90) """
    
# Mit der Turtle alles von Dreieck bis Zehneck in Regenbogenfarben zeichen

corners = 3
sum_angles = 360
turtle_movespeed = 80

while corners <= 10:
    for _ in range(corners):
        myDudu.pensize(5)
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
        myDudu.pencolor(random.choice(color_list))
    corners += 1
    
    # Ignore this unholiness
    """ for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
    corners += 1
    for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
    corners += 1
    for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
    corners += 1
    for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
    corners += 1
    for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
    corners += 1
    for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners)
    corners += 1
    for _ in range(corners):
        myDudu.fd(turtle_movespeed)
        myDudu.left(sum_angles / corners) """    
    


# # # WICHTIG # # #
#     Damit sich der Screen nicht sofort wieder schließt, sondern erst beim Klick auf das X
screen.exitonclick()