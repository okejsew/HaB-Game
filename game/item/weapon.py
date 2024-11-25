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
            # Если брони нет, или она сломана
            # Урон = урон оружия * 2
            whom.health.change(-self.damage * 2, bodypart)
            return

        # diff = Разница между фактором брони и фактором оружия
        difference = abs(self.factor - armor.factor)

        # Урон = урон оружия / (diff + 1)
        if armor.factor > self.factor:
            damage = round(self.damage / (difference + 1))
            # Урон оружию = 1 + diff * 2
            self.change(-(1 + difference * 2))

        # Урон = урон оружия + (урон оружия * 2 / diff)
        elif armor.factor < self.factor:
            damage = round(self.damage + self.damage / 2 * difference)
            self.change(-randint(0, 1))

        else:  # Урон = урон оружия
            damage = self.damage
            self.change(-1)
        whom.health.change(-damage, bodypart)
        armor.on_attack(who, whom, bodypart, self, damage)

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.name}'
