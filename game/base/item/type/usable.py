from game.base.item.item import Item


class Usable(Item):
    def __init__(self, name: str = 'Usable'):
        super().__init__(name)
        self.usages = 10
        self.max_usages = 10