from game.entity.player import Player
from game.item.armor import BodyPart, Armor
from game.item.weapon import Weapon
from game.manager.battle import BattleManager
from game.manager.ui import UIManager


class Game:
    def __init__(self):
        self.player = Player()
        self.ui = UIManager(self)
        self.battle = BattleManager(self)

    def attack(self):
        self.player.attack(self.player, BodyPart.chest)

    def start(self):
        self.player.equip(Armor())
        self.player.equip(Weapon())
        self.player.equipment.chest.factor = 10
        self.attack()
        print(self.player)
