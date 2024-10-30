from game.base.equipment import Equipment
from game.base.inventory import Inventory


class Player:
    def __init__(self):
        self.name: str = 'Player'
        self.inventory: Inventory = Inventory()
        self.inventory.player = self
        self.equipment: Equipment = Equipment()
