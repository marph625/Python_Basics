from character import Character

# objects

hero = Character(name="Gregor", health=100)
enemy = Character("Hugo", 100)

# main loop

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"{hero.name}:{hero.health}")
    print(f"{enemy.name}:{enemy.health}")

    # Makes the infinite loop less scary
    input()