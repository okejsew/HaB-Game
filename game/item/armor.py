from enum import Enum
from random import randint
from typing import TYPE_CHECKING

from game.item.battle import BattleItem
from game.tools.math import percent

if TYPE_CHECKING:
    from game.item.weapon import Weapon
    from game.entity import BaseEntity


class BodyPart(Enum):
    head = 1
    hands = 3
    chest = 2
    legs = 4
    feet = 5


class Armor(BattleItem):
    def __init__(self):
        super().__init__()
        self.name = 'Броня'
        self.type = BodyPart.chest

    def on_attack(self, who: 'BaseEntity', whom: 'BaseEntity', bodypart: 'BodyPart', weapon: 'Weapon', damage: int):
        # diff = Разница между фактором защиты и фактором атаки
        difference = abs(self.factor - weapon.factor)

        if weapon.factor > self.factor:
            # Урон броне = (diff * 2) + 1 + 2% урона
            self.change(-(1 + difference * 2 + percent(damage, 2)))
            who.health.change(1, BodyPart.head)

        elif weapon.factor < self.factor:
            # Урон броне = 1 или 0 (хз лол)
            self.change(-randint(0, 1))

        else:
            # Урон броне = 1 + 1% урона
            self.change(-(1 + percent(damage, 1)))

        # Дополнительно наносимый урон (cuz конечности связяны)
        match bodypart:
            case BodyPart.head:
                whom.health.change(-percent(damage, 35), BodyPart.chest)
            case BodyPart.chest:
                whom.health.change(-percent(damage, 25), BodyPart.hands)
                whom.health.change(-percent(damage, 15), BodyPart.head)
                whom.health.change(-percent(damage, 20), BodyPart.legs)
            case BodyPart.legs:
                whom.health.change(-percent(damage, 15), BodyPart.chest)
                whom.health.change(-percent(damage, 25), BodyPart.feet)

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.name}'
