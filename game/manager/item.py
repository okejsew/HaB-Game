from typing import Optional
from uuid import uuid4, UUID

from game.base.item import Item


class ItemManager:
    entities: dict[UUID, Item] = {}

    @staticmethod
    def register(new: Item):
        new.id = uuid4()
        ItemManager.entities[new.id] = new

    @staticmethod
    def get(uuid: UUID) -> Optional[Item]:
        return ItemManager.entities[uuid]
