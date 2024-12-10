from game.items.wearable import Wearable


class Armor(Wearable):
    def __init__(self, name: str = 'Armor'):
        super().__init__(name)
        self.factor: int = 1
        self.bodypart: str = 'chest'

    def on_attack(self, who: 'Entity', weapon: 'Weapon', damage: int):
        self.durablity['current'] -= 1
        self.owner.hurt(damage, self.bodypart)
        who.heal(1, 'head')

    def __repr__(self):
        return super().__repr__() + f'[factor={self.factor}]'


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.items.weapon import Weapon
    from game.base.entity import Entity
