import os
from character import Hero, Enemy
from weapon import short_bow, iron_sword

# objects

hero = Hero(name="Gregor", health=100)
enemy = Enemy(name="Hugo", health=100, weapon=short_bow)
hero.equip(iron_sword)

# main loop

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    # Makes the infinite loop less scary
    input()