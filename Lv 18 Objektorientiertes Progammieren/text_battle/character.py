from weapon import fists
from health_bar import HealthBar

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
        target.health_bar.update()
        print(f"{self.name} dealt {self.weapon.damage} damage to " 
        f"{target.name} with {self.weapon.name}")

class Hero(Character):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name=name, health=health)

        self.default_weapon = self.weapon
        self.health_bar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped {self.weapon.name}!")

    def drop(self) -> None:
        self.weapon = self.default_weapon
        print(f"{self.name} dropped {self.weapon.name}!")

class Enemy(Character):
    def __init__(self, name: str, health: int, weapon: str) -> None:
        super().__init__(name=name, health=health)

        self.weapon = weapon
        self.health_bar = HealthBar(self, color="red")