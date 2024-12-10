from traceback import print_exception

from game.base.entity import Entity
from game.items.armor import Armor
from game.items.weapon import Weapon

try:
    w = Weapon()
    a = Armor()
    ply = Entity('Player')
    ply.equip(w)
    ply.equip(a)

    ply.attack(ply)
    print(w)
    print(a)
    print(ply)


except Exception as ex:
    print_exception(ex)