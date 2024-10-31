import curses
from webbrowser import Galeon

from game.base.player import Player
from game.localization import Locale
from tui import Tui
from tui.elements.button import Button
from tui.fabric import TuiFabric


class Menu:
    main: Tui

    @staticmethod
    def setup():
        Menu.main = TuiFabric.load('game/resources/ui/main.tui')
        Menu.main.get('btn_exit', Button).click = HaB.exit


class HaB:
    player: Player = Player()

    @staticmethod
    def exit():
        curses.endwin()
        Tui.end()
        exit()

    @staticmethod
    def init():
        Locale.load('ru')
        Menu.setup()

    @staticmethod
    def start():
        Menu.main.show()
