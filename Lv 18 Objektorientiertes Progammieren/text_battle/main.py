import os
from character import *
from weapon import *

# objects

hero = Hero(name="Gregor", health=100)
enemy = Enemy(name="Hugo", health=100, weapon=short_bow)
dragon = Dragon(name="Norbert", health=1000, weapon=dragons_breath)
hero.equip(magic_staff)

# main loop

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if hero.health == 0:
        print("Game Over")
        break

    if enemy.health == 0:
        hero.attack(dragon)
        dragon.attack(hero)
        hero.health_bar.draw()
        dragon.health_bar.draw()


    # Makes the infinite loop less scary
    input()