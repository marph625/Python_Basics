from weapon import fists

class Character:
    # Class Level Variables
    # race = "Human"

    def __init__(self, name: str, health: int):
        # Object Level Variables
        self.name = name
        self.health = health
        self.health_max = health
        self.weapon = fists

    def attack(self, target):
        target.health -= self.weapon.damage
        # if target.hp is negative, it will be set to 0
        target.health = max(target.health, 0)