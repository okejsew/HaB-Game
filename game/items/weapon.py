from game.items.wearable import Wearable


class Weapon(Wearable):
    def __init__(self, name: str = 'Weapon'):
        super().__init__(name)
        self.damage: int = 10

    def attack(self, whom: 'Entity', bodypart: str):
        self.durablity['current'] -= 1
        armor = whom.equipment[bodypart]
        armor.on_attack(self.owner, self, self.damage)

    def __repr__(self):
        return super().__repr__() + f'[dmg={self.damage}]'


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.base.entity import Entity
