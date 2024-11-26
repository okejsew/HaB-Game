from dataclasses import dataclass
from typing import Optional, Callable

from game.base.item import Item, Armor, Weapon, Usable
from game.core.bodypart import BodyPart


@dataclass
class Equipment:
    head: Optional[Armor] = None
    hands: Optional[Armor] = None
    chest: Optional[Armor] = None
    legs: Optional[Armor] = None
    feet: Optional[Armor] = None

    right_hand: Optional[Weapon] = None
    left_hand: Optional[Usable] = None

    def equip(self, item: Item, add_method: Callable[[Item], None]):
        if isinstance(item, Armor):
            if prev := getattr(self, item.bodypart.name):
                add_method(prev)
            setattr(self, item.bodypart.name, item)
        elif isinstance(item, Weapon):
            if self.right_hand:
                add_method(self.right_hand)
            self.right_hand = item
        elif isinstance(item, Usable):
            if self.left_hand:
                add_method(self.left_hand)
            self.left_hand = item

    def get(self, bodypart: BodyPart) -> Armor:
        return getattr(self, bodypart.name)

    def __repr__(self):
        string = f'    Голова: {self.head}\n'
        string += f'    Руки: {self.hands}\n'
        string += f'    Живот: {self.chest}\n'
        string += f'    Ноги: {self.legs}\n'
        string += f'    Ступни: {self.feet}\n'
        string += '    ---------------\n'
        string += f'    Правая рука: {self.right_hand}\n'
        string += f'    Левая рука: {self.left_hand}\n'
        return string
