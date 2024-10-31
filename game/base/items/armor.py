from game.base.item import BaseItem


class ArmorType:
    head = 1
    hands = 3
    chest = 2
    legs = 4
    feet = 5


class Armor(BaseItem):
    def __init__(self):
        super().__init__()
        self.type = ArmorType.head
        self.durability: int = 0
        self.max_durability: int = 100
        self.protect_factor: int = 10

    def on_hit(self): ...

    def __str__(self):
        return f'{self.name} [{self.durability} / {self.max_durability}]'
