from typing import TYPE_CHECKING

from game.item.armor import Armor
from game.item.usable import Usable
from game.item.weapon import Weapon

if TYPE_CHECKING:
    from game.item.armor import BodyPart
from game.entity.params.equipment import Equipment
from game.entity.params.health import Health
from game.item import BaseItem


class BaseEntity:
    def __init__(self):
        self.name = 'Базовая сущность'
        self.health = Health()
        self.equipment = Equipment(self)
        self.inventory: list[BaseItem] = []

    def attack(self, whom: 'BaseEntity', bodypart: 'BodyPart'):
        if self.equipment.right_hand:
            self.equipment.right_hand.attack(self, whom, bodypart)

    def equip(self, item: BaseItem):
        if isinstance(item, Weapon):
            if self.equipment.right_hand:
                self.inventory.append(self.equipment.right_hand)
                self.equipment.right_hand = None
            self.equipment.right_hand = item
        elif isinstance(item, Armor):
            if armor := getattr(self.equipment, item.type.name):
                self.inventory.append(armor)
                setattr(self.equipment, item.type.name, None)
            setattr(self.equipment, item.type.name, item)
        elif isinstance(item, Usable):
            if self.equipment.left_hand:
                self.inventory.append(self.equipment.left_hand)
                self.equipment.left_hand = None
            self.equipment.left_hand = item
