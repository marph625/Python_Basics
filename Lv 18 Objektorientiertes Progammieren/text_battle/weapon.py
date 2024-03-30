class Weapon:
    def __init__(
        self, name: str,
        weapon_type: str,
        rarity: str,
        damage: int,
        value: int) -> None:

        self.name = name
        self.weapon_type = weapon_type
        self.rarity = rarity
        self.damage = damage
        self.value = value

dragons_breath = Weapon(
    name="Dragon's Breath",
    weapon_type="elemental",
    rarity="legendary",
    damage=25,
    value=100
)

magic_staff = Weapon(
    name="Wizard's Staff",
    weapon_type="magic",
    rarity="epic",
    damage=15,
    value=40
)

great_axe = Weapon(
    name="Great Axe",
    weapon_type="sharp",
    rarity="rare",
    damage=8,
    value=20
)

iron_sword = Weapon(
    name="Iron Sword",
    weapon_type="sharp",
    rarity="uncommon",
    damage=5,
    value=10 
)

short_bow = Weapon(
    name="Short Bow",
    weapon_type="ranged",
    rarity="uncommon",
    damage=4,
    value=8
)

fists = Weapon(
    name="Fists",
    weapon_type="blunt",
    rarity="common",
    damage=2,
    value=0
)