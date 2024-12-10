from game.base.item import Item
from tools.loader import loader


class Wearable(Item):
    def __init__(self, name: str = 'Wearable'):
        super().__init__(name)
        self.durablity: dict[str, int] = loader('durability')

    def fracture(self, amount: int):
        new_hp = max(0, self.durablity['current'] - amount)
        self.durablity['current'] = new_hp

    def repair(self, amount: int):
        new_hp = min(self.durablity['max'], self.durablity['current'] + amount)
        self.durablity['current'] = new_hp

    def __repr__(self):
        return super().__repr__() + f' [dur={self.durablity["current"]}/{self.durablity["max"]}]'

