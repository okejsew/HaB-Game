from game.base.item import BaseItem
from game.items.weapon.menu import WeaponContextMenu


class Weapon(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'weapon'
        self.context_menu = WeaponContextMenu(self)

        self.durability: int = 0
        self.max_durability: int = 100
        self.damage: int = 10

    def equip(self):
        ...

    def on_attack(self): ...

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.get_name()}'
