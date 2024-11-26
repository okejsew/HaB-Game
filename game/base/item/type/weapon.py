from uuid import UUID

from game.base.item import BodyPart
from game.base.item.item import Wearable


class Weapon(Wearable):
    def __init__(self, name: str = 'Weapon'):
        super().__init__(name)
        self.damage = 10

    def attack(self, whom: UUID, bodypart: BodyPart):
        from game.manager.entity import EntityManager
        whom = EntityManager.get(whom)

        whom.health.damage(self.damage, bodypart)
        return self.damage
