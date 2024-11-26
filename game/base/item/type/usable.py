from game.base.item.item import Item


class Usable(Item):
    def __init__(self, name: str = 'Usable'):
        super().__init__(name)
        self.usages: int = 10
        self.max_usages: int = 10

    def __repr__(self):
        return super().__repr__() + f'[{self.usages}/{self.max_usages}]'
