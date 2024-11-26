from game.base.entity.health import Health
from game.base.entity.equip import Equipment
from game.base.item import Item, BodyPart
from game.core.object import Object


class Entity(Object):
    def __init__(self, name: str = 'Entity'):
        super().__init__(name)
        self.health = Health()
        self.equipment = Equipment()
        self.inventory: list[Item] = []

    def add_item(self, item: Item):
        if item not in self.inventory:
            self.inventory.append(item)
            item.owner_id = self.id

    def equip_item(self, item: Item):
        item.owner_id = self.id
        if item in self.inventory:
            self.inventory.remove(item)
        self.equipment.equip(item, self.inventory)
