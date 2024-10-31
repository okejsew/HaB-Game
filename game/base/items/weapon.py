from game.base.item import BaseItem


class Weapon(BaseItem):
    def __init__(self):
        super().__init__()
        self.durability: int = 0
        self.max_durability: int = 100
        self.damage: int = 10

    def on_attack(self): ...

    def __str__(self):
        return f'{self.name} [{self.durability} / {self.max_durability}]'
