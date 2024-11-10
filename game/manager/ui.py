from tui.fabric import TuiFabric
from tui import Tui

from game.manager import singleton

@singleton
class UIManager:
    def __init__(self):
        self.menu_main: Tui = TuiFabric.load('resources/ui/main.tui')

    def start(self):
        self.menu_main.show()