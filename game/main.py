import curses

from game.base.player import Player
from game.utils.localization import Locale
from game.utils.tui import Tui, Button

menu_main = Tui()
player = Player()


def exit_game():
    curses.endwin()
    Tui.end()
    exit()


def load():
    Locale.load('ru')
    menu_main.load('game/resources/ui/main.tui')
    menu_main.get('btn_exit', Button).click = exit_game
