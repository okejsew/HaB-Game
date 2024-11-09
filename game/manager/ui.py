from tui.fabric import TuiFabric
from tui import Tui

from game.manager import SingletonManager


class UIManager(SingletonManager):
    def __init__(self):
        super().__init__()
        self.menu_main: Tui = TuiFabric.load('resources/ui/main.tui')

    def start(self):
        self.menu_main.show()