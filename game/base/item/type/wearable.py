from game.base.item.item import Item


class Wearable(Item):
    def __init__(self, name: str = 'Wearable'):
        super().__init__(name)
        self.durability: int = 50
        self.max_durability: int = 50
        self.cls: int = 1

    def repair(self, amount: int):
        self.durability = min(self.max_durability, self.durability + amount)

    def damage(self, amount: int):
        self.durability = max(0, self.durability - amount)

    def __repr__(self):
        return super().__repr__() + f'[{self.durability}/{self.max_durability}][CLS={self.cls}]'
