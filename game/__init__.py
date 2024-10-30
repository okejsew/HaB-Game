import curses

from game.base.player import Player
from game.utils.localization import Locale
from game.utils.tui import Tui, Button


class Game:
    player: Player = Player()

    @staticmethod
    def exit():
        curses.endwin()
        Tui.end()
        exit()


class Interface:
    main: Tui = Tui()

    @staticmethod
    def setup():
        Interface.main.load('game/resources/ui/main.tui')
        Interface.main.get('btn_exit', Button).click = Game.exit
        Interface.main.get('btn_inventory', Button).click = Game.player.inventory.open


def init():
    Locale.load('ru')
    Interface.setup()


def start():
    Interface.main.show()
