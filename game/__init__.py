import curses
import random

from game.entities.player import Player
from game.base.item import BaseItem
from game.items.armor import Armor
from game.items.usable import Usable
from game.items.weapon import Weapon
from localization import Locale
from utils.dialog import DialogFabric
from utils.tui import Tui


class Game:
    player: Player = Player()

    @staticmethod
    def exit():
        curses.endwin()
        Tui.end()
        exit()

    @staticmethod
    def add_item(item: BaseItem):
        if item not in Game.player.inventory:
            Game.player.inventory.append(item)
            item.owner = Game.player

    @staticmethod
    def init():
        from game.interface import Menu
        Locale.load('en')
        Game.add_item(BaseItem())
        Game.add_item(Weapon())
        Game.add_item(Armor())
        Game.add_item(Usable())
        Menu.setup()

    @staticmethod
    def start():
        from game.interface import Menu
        DialogFabric.load(f'greeting{random.randint(2, 4)}').start()
        Menu.main.show()
