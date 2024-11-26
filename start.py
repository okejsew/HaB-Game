from traceback import print_exception

from game import *


try:
    ply = Entity('Player')
    w = Weapon('Деревянный меч')
    a = Armor('Деревянная броня')
    u = Usable('Ягоды')

    ply.equip(w)
    ply.equip(a)
    ply.equip(u)

    BattleManager.attack(ply, ply, BodyPart.chest)
    print(ply)
    input()
except Exception as ex:
    print_exception(ex)
    input()