from uuid import UUID

from game.base.item.bodypart import BodyPart
from game.base.item.item import Wearable



class Armor(Wearable):
    def __init__(self):
        super().__init__()
        self.type = BodyPart.chest

    def on_attack(self, who: UUID, bodypart: BodyPart, damage: int):
        from game.manager.entity import EntityManager
        who = EntityManager.get(who)
        who.health.heal(damage + self.durability, bodypart)