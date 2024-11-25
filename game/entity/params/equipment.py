from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from game.entity import BaseEntity
from game.item import BaseItem
from game.item.armor import Armor, BodyPart
from game.item.usable import Usable
from game.item.weapon import Weapon


class Equipment:
    def __init__(self, owner: 'BaseEntity'):
        self.owner = owner
        self.head: Optional[Armor] = None
        self.hands: Optional[Armor] = None
        self.chest: Optional[Armor] = None
        self.legs: Optional[Armor] = None
        self.feet: Optional[Armor] = None

        self.right_hand: Optional[Weapon] = None
        self.left_hand: Optional[Usable] = None

    def get(self, bodypart: BodyPart) -> Armor | None:
        return getattr(self, bodypart.name)

    def __str__(self):
        return f"""
    Голова  - {self.head}
    Руки    - {self.hands} 
    Тело    - {self.chest}
    Ноги    - {self.legs}
    Ступни  - {self.feet}
    -------------
    Правая рука - {self.right_hand}
    Левая рука  - {self.left_hand}"""
