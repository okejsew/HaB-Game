import curses

from game.entities.player import Player
from game.base.item import BaseItem
from game.items.armor import Armor
from game.items.usable import Usable
from game.items.weapon import Weapon
from localization import Locale
from tui import Tui


class HaB:
    player: Player = Player()

    @staticmethod
    def exit():
        curses.endwin()
        Tui.end()
        exit()

    @staticmethod
    def add_item(item: BaseItem):
        if item not in HaB.player.inventory:
            HaB.player.inventory.append(item)
            item.owner = HaB.player

    @staticmethod
    def init():
        from game.interface import Menu
        Locale.load('en')
        HaB.add_item(BaseItem())
        HaB.add_item(Weapon())
        HaB.add_item(Armor())
        HaB.add_item(Usable())
        Menu.setup()

    @staticmethod
    def start():
        from game.interface import Menu
        Menu.main.show()
