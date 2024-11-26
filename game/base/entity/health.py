from dataclasses import dataclass

from game.core.bodypart import BodyPart


@dataclass
class Health:
    head = 40
    chest = 50
    hands = 30
    legs = 40
    feet = 25

    head_max = 40
    chest_max = 50
    hands_max = 30
    legs_max = 40
    feet_max = 25

    def damage(self, amount: int, bodypart: BodyPart):
        new_hp = max(0, getattr(self, bodypart.name) - amount)
        setattr(self, bodypart.name, new_hp)

    def heal(self, amount: int, bodypart: BodyPart):
        max_hp = getattr(self, bodypart.name + '_max')
        new_hp = min(max_hp, getattr(self, bodypart.name) + amount)
        setattr(self, bodypart.name, new_hp)

    def __repr__(self):
        string = f'    Голова: {self.head}/{self.head_max}\n'
        string += f'    Живот: {self.chest}/{self.chest_max}\n'
        string += f'    Руки: {self.hands}/{self.hands_max}\n'
        string += f'    Ноги: {self.legs}/{self.legs_max}\n'
        string += f'    Ступни: {self.feet}/{self.feet_max}\n'
        return string