# # # # Lv 16 OOP Script 1 # # # #

# 1 # # turtle Import # # # #
from turtle import Turtle, Screen

# 2 # # Objekt Deklaration # # # #
my_dude = Turtle()
dudes_screen = Screen()

# 3 # # Zeigen an welcher Stelle auf dem Speicher das Objekt abgelegt wird # # # #
print(my_dude)

# 4 # # hier muss der Screen importiert sein (mit import * geloest aber from turtle import Screen wäre besser) # # # #
# # # # Zugriff auf die Attribute eines Objektes mit object.attribute# # # #
print(dudes_screen.canvheight)

# 5 # # Zugriff auf die Methode eines Objektes # # # #
dudes_screen.exitonclick()

##########################################################################################

# 6 # # Nach der Erläuterung zur exitonclick() Methode # # # #
my_dude.shape("turtle")

# 7 # # Miniaufgabe anhand der Dokumentation die Farbe der Schildkröte ändern # # # #
# 8 # # Miniaufgabe die Schildkröte in einem Rechteck bewegen, jede Seite des Rechtecks hat 100 Einheiten # # # #


##########################################################################################
