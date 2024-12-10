from game.base.object import Object
from game.items.wearable import Wearable
from tools.loader import loader


class Entity(Object):
    def __init__(self, name: str = 'Entity'):
        super().__init__(name)
        self.inventory: list[Item] = []
        self.equipment: dict[str, Armor | None] = loader('equipment')
        self.health: dict[str, int] = loader('health')
        self.hand: Weapon | None = None

    def equip(self, item: Wearable):
        from game.items.armor import Armor
        from game.items.weapon import Weapon
        if isinstance(item, Weapon):
            if self.hand is item: return
            if prev := self.hand: self.add(prev)
            self.hand = item
        elif isinstance(item, Armor):
            if prev := self.equipment[item.bodypart] is item: return
            if prev: self.add(prev)
            self.equipment[item.bodypart] = item
        if item in self.inventory:
            self.inventory.remove(item)
        item.owner = self

    def add(self, item: 'Item'):
        if item not in self.inventory:
            self.inventory.append(item)
            item.owner = self

    def hurt(self, amount: int, bodypart: str):
        new_hp = max(0, self.health[bodypart] - amount)
        self.health[bodypart] = new_hp

    def heal(self, amount: int, bodypart: str):
        max_hp = self.health[bodypart + '_max']
        new_hp = min(max_hp, self.health[bodypart] + amount)
        self.health[bodypart] = new_hp

    def attack(self, whom: 'Entity', bodypart: str = 'chest'):
        if self.hand:
            self.hand.attack(whom, bodypart)
        else:
            whom.health[bodypart] -= 1

    def __repr__(self):
        string = super().__repr__()
        string += f' [inv={len(self.inventory)}] '
        for bodypart, amount in self.health.items():
            if '_max' not in bodypart:
                string += f'[{bodypart}='
                string += f'{amount}/{self.health[bodypart + "_max"]}]'
        return string


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from game.base.item import Item
    from game.items.armor import Armor
    from game.items.weapon import Weapon
