from TurtleRacer_class import TurtleRacer, FastTurtleRacer

turbo_racer = FastTurtleRacer("purple", (-100, 60), 10)

racers = [
    TurtleRacer("red", (-100, 20)),
    TurtleRacer("blue", (-100, -20)),
    TurtleRacer("green", (-100, -60)),
    turbo_racer
]

for _ in range(70):
    for racer in racers:
        racer.race()

turtle.done()