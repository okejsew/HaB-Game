from typing import TYPE_CHECKING, Optional

from game.base.item import BaseItem
from game.utils.localization import Locale
from game.utils.tui import Tui, Label, Button

if TYPE_CHECKING:
    from game.base.player import Player


class Inventory:
    def __init__(self):
        self.player: Optional['Player'] = None
        self.items: list[BaseItem] = []

    def open(self):
        from game import Interface
        tui = Tui()
        tui.add(Label(Locale.get('inventory') + self.player.name))
        self.update_items(tui)
        tui.add(Button(Locale.get('back'), Interface.main.show))
        tui.show()

    def update_items(self, tui: Tui):
        ...
