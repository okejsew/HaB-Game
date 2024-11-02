from typing import TYPE_CHECKING

from game.base.item import ItemContextMenu
from localization import Locale
from tui.elements.button import Button

if TYPE_CHECKING:
    from game.items.usable import Usable


class UsableContextMenu(ItemContextMenu):
    def __init__(self, item: 'Usable'):
        super().__init__(item)
        self.add(Button(Locale.get("use"), item.use))
