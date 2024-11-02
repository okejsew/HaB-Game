from typing import TYPE_CHECKING

from game.base.item import ItemContextMenu
from localization import Locale
from tui.elements.button import Button

if TYPE_CHECKING:
    from game.items.armor import Armor


class ArmorContextMenu(ItemContextMenu):
    def __init__(self, item: 'Armor'):
        super().__init__(item)
        self.add(Button(Locale.get("equip"), item.equip))
