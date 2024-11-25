from game.entity.params.equipment import Equipment
from game.entity.params.health import Health
from game.item import BaseItem


class BaseEntity:
    def __init__(self):
        self.name = 'Базовая сущность'
        self.health = Health()
        self.equipment = Equipment()
        self.inventory: list[BaseItem] = []
