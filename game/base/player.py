from game.base.equipment import Equipment
from game.base.inventory import Inventory


class Player:
    def __init__(self):
        self.inventory: Inventory = Inventory()
        self.equipment: Equipment = Equipment()