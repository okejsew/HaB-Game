from game.base.entity import Entity
from game.core.bodypart import BodyPart


class BattleManager:
    @staticmethod
    def attack(who: Entity, whom: Entity, bodypart: BodyPart):
        weapon = who.equipment.right_hand
        armor = whom.equipment.get(bodypart)
        armor.on_attack(who, weapon.attack(whom, bodypart))