from typing import TYPE_CHECKING

from game.base.item.type.wearable import Wearable
from game.core.bodypart import BodyPart

if TYPE_CHECKING:
    from game.base.entity import Entity


class Armor(Wearable):
    def __init__(self, name: str = 'Armor'):
        super().__init__(name)
        self.bodypart: BodyPart = BodyPart.chest

    def __repr__(self):
        return super().__repr__() + f'[BP={self.bodypart.name}]'

    def on_attack(self, who: 'Entity', damage):
        pass
