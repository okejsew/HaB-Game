from typing import Optional, TYPE_CHECKING

from game.base.baseitem import Weapon, Armor

if TYPE_CHECKING:
    from game.base.player import Player


class Gear:
    def __init__(self):
        self.head: Optional[Armor] = None
        self.hands: Optional[Armor] = None
        self.chest: Optional[Armor] = None
        self.legs: Optional[Armor] = None
        self.feet: Optional[Armor] = None


class Equipment:
    def __init__(self):
        self.player: Optional['Player'] = None
        self.gear: Gear = Gear()
        self.primary: Optional[Weapon] = None
        self.secondary: Optional[Weapon] = None
