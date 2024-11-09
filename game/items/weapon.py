from game.base.item import BaseItem


class Weapon(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'weapon'

        self.durability: int = 0
        self.max_durability: int = 100
        self.damage: int = 10

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.name}'
