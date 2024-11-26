from typing import Optional
from uuid import uuid4, UUID

from game.base.entity import Entity


class EntityManager:
    entities: dict[UUID, Entity] = {}

    @staticmethod
    def register(new: Entity):
        new.id = uuid4()
        EntityManager.entities[new.id] = new

    @staticmethod
    def get(uuid: UUID) -> Optional[Entity]:
        return EntityManager.entities[uuid]
