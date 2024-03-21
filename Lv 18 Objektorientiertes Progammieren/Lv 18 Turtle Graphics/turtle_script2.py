# Nochmal ganz in Ruhe..

# 1. Turtle importieren
import turtle
from turtle import *

# 2. Objekt Deklaration

freddy_the_turtle = Turtle()
screen = Screen()

# 3. Zeigen an welcher Stelle auf dem Speicher das Objekt abgelegt wird

print(freddy_the_turtle)

# 4. Hier muss der Screen importiert sein (mit import * geloest aber from turtle import Screen wäre besser) # # # #
# Zugriff auf die Attribute eines Objektes mit object.attribute()

print(screen.canvheight)

# 5. Zugriff auf die Methode eines Objektes
screen.exitonclick()

# 6. Mittels object.attribute() die Form des Objektes definieren
freddy_the_turtle.shape("turtle")

# 7. Miniaufgabe anhand der Dokumentation die Farbe der Schildkröte ändern
freddy_the_turtle.color("red")
# 8. Miniaufgabe die Schildkröte in einem Rechteck bewegen, jede Seite des Rechtecks hat 100 Einheiten
freddy_the_turtle.fd(100)
freddy_the_turtle.left(90)
freddy_the_turtle.fd(100)
freddy_the_turtle.left(90)
freddy_the_turtle.fd(100)
freddy_the_turtle.left(90)
freddy_the_turtle.fd(100)

turtle.mainloop()