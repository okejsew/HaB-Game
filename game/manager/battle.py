from game.base.entity import Entity
from game.base.item import BodyPart


class BattleManager:
    @staticmethod
    def attack(who: Entity, whom: Entity, bodypart: BodyPart):
        if weapon := who.equipment.right_hand:
            damage = weapon.attack(whom.id, bodypart)
            if not damage: return
            if armor := whom.equipment.get(bodypart):
                armor.on_attack(who.id, bodypart, damage)