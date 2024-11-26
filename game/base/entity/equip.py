from typing import Optional

from game.base.item import Armor, Weapon, Usable, Item


class Equipment:
    def __init__(self):
        self.head: Optional[Armor] = None
        self.hands: Optional[Armor] = None
        self.chest: Optional[Armor] = None
        self.legs: Optional[Armor] = None
        self.feet: Optional[Armor] = None

        self.right_hand: Optional[Weapon] = None
        self.left_hand: Optional[Usable] = None

    def equip(self, item: Item, return_to: list[Item]):
        if isinstance(item, Armor):
            if equiped_item := getattr(self, item.type.name):
                return_to.append(equiped_item)
            setattr(self, item.type.name, item)
        elif isinstance(item, Weapon):
            if self.right_hand:
                return_to.append(self.right_hand)
            self.right_hand = item
        elif isinstance(item, Usable):
            if self.left_hand:
                return_to.append(self.left_hand)
            self.left_hand = item

    def get(self, bodypart) -> Armor:
        return getattr(self, bodypart.name)

