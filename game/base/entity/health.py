from dataclasses import dataclass

from game.core.bodypart import BodyPart
from game.core.settings import Settings


@dataclass
class Health:
    head: int = 40
    chest: int = 50
    hands: int = 30
    legs: int = 40
    feet: int = 25

    head_max: int = 40
    chest_max: int = 50
    hands_max: int = 30
    legs_max: int = 40
    feet_max: int = 25

    def damage(self, amount: int, bodypart: BodyPart):
        new_hp = max(0, getattr(self, bodypart.name) - amount)
        setattr(self, bodypart.name, int(new_hp))

    def heal(self, amount: int, bodypart: BodyPart):
        max_hp = getattr(self, bodypart.name + '_max')
        new_hp = min(max_hp, getattr(self, bodypart.name) + amount)
        setattr(self, bodypart.name, int(new_hp))

    def __repr__(self):
        string = ''
        for bodypart, health in self.__dict__.items():
            if '_max' not in bodypart:
                string += f'    {getattr(BodyPart, bodypart).value}: '.ljust(Settings.ljust_health)
                string += f'{health}/{getattr(self, bodypart + "_max")}\n'
        return string