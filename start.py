from game.base.entity import Entity
from game.base.item import Armor, Weapon, BodyPart
from game.manager.battle import BattleManager
from game.manager.entity import EntityManager
from game.manager.item import ItemManager

ply = Entity()
armor = Armor()
weapon = Weapon()

EntityManager.register(ply)
ItemManager.register(armor)
ItemManager.register(weapon)

ply.equip_item(armor)
ply.equip_item(weapon)

BattleManager.attack(ply, ply, BodyPart.chest)
print(ply)