from typing import Optional
from uuid import UUID

from game.base.item.rarity import Rarity
from game.core.object import Object


class Item(Object):
    def __init__(self, name: str = 'Item'):
        super().__init__(name)
        self.owner_id: Optional[UUID] = None
        self.rarity = Rarity.Common


class Wearable(Item):
    def __init__(self, name: str = 'Wearable'):
        super().__init__(name)
        self.durability = 50
        self.max_durability = 50
        self.battle_factor = 1
