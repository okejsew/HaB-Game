from typing import TYPE_CHECKING

from game.base.entity.equip import Equipment
from game.base.entity.health import Health
from game.core.object import Object

if TYPE_CHECKING:
    from game.base.item import Item


class Entity(Object):
    def __init__(self, name: str = 'Entity'):
        super().__init__(name)
        self.inventory: list['Item'] = []
        self.equipment: Equipment = Equipment()
        self.health: Health = Health()

    def add(self, item: 'Item'):
        if item not in self.inventory:
            self.inventory.append(item)
            item.owner = self

    def equip(self, item: 'Item'):
        item.owner = self
        if item in self.inventory:
            self.inventory.remove(item)
        self.equipment.equip(item, self.add)

    def __repr__(self):
        string = super().__repr__()
        string += '\n\n  Снаряжение:\n' + repr(self.equipment)
        string += f'\n  Инвентарь: {self.inventory}\n'
        string += f'\n  Здоровье:\n' + repr(self.health)
        return string
