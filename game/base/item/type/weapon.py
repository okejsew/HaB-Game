from typing import TYPE_CHECKING

from game.base.item.type.wearable import Wearable
from game.core.bodypart import BodyPart

if TYPE_CHECKING:
    from game.base.entity import Entity


class Weapon(Wearable):
    def __init__(self, name: str = 'Weapon'):
        super().__init__(name)
        self.damage: int = 10

    def __repr__(self):
        return super().__repr__() + f'[DMG={self.damage}]'

    def attack(self, whom: 'Entity', bodypart: BodyPart) -> int:
        pass
