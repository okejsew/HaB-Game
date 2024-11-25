from random import randint
from typing import TYPE_CHECKING

from game.item.battle import BattleItem

if TYPE_CHECKING:
    from game.entity import BaseEntity
    from game.item.armor import BodyPart


class Weapon(BattleItem):
    def __init__(self):
        super().__init__()
        self.name = 'Оружие'
        self.damage = 10

    def attack(self, who: 'BaseEntity', whom: 'BaseEntity', bodypart: 'BodyPart'):
        armor = whom.equipment.get(bodypart)
        if not armor or armor.durability == 0:
            whom.health.change(-self.damage * 2, bodypart)
            return
        difference = abs(self.factor - armor.factor)
        if armor.factor > self.factor:  # Если класс у брони больше
            damage = round(self.damage / (difference + 1))
            self.durability -= (1 + difference * 2)
        elif armor.factor < self.factor:  # Если класс у оружия больше
            damage = round(self.damage + self.damage / 2 * difference)
            self.durability -= randint(0, 1)
        else:  # Если класс брони такой же, как и у оружия
            damage = self.damage
            self.durability -= 1
        whom.health.change(-damage, bodypart)
        armor.on_attack(who, whom, bodypart, self, damage)

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.name}'
