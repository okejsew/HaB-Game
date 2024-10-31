from game.entity.health import Health
from game.base.item import BaseItem


class BaseEntity:
    def __init__(self):
        self.name: str = 'Entity'
        self.health: Health = Health()
        self.inventory: list[BaseItem] = []

