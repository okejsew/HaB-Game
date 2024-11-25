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
        self.player.equipment.right_hand.attack(self.player, self.player, BodyPart.chest)

    def start(self):
        self.player.equipment.chest = Armor()
        self.player.equipment.right_hand = Weapon()
        self.player.equipment.right_hand.factor = 10
        self.attack()
        self.attack()
        self.attack()
        print(self.player)
