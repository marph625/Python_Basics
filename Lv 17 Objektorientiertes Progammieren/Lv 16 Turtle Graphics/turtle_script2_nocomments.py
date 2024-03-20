import turtle

freddy_the_turtle = turtle.Turtle()
screen = turtle.Screen()

print(freddy_the_turtle)
print(screen.canvheight)

screen.exitonclick()

freddy_the_turtle.shape("turtle")
freddy_the_turtle.color("red")

freddy_the_turtle.fd(100)
freddy_the_turtle.left(90)
freddy_the_turtle.fd(100)
freddy_the_turtle.left(90)
freddy_the_turtle.fd(100)
freddy_the_turtle.left(90)
freddy_the_turtle.fd(100)

screen.update()