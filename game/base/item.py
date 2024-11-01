from enum import Enum

from game.localization import Locale
from tui import BaseElement
from tui.elements.label import Label
from tui.elements.splitter import Splitter


class ItemContextMenu:
    def __init__(self, item: 'BaseItem'):
        self.item = item
        self.elements: list[BaseElement] = []
        self.add(Label(self.item.get_name()))
        self.add(Splitter())
        self.add(Label(f'{Locale.get("description")}:'))
        self.add(Label(self.item.get_description()))
        self.add(Splitter())

    def add(self, element: BaseElement):
        self.elements.append(element)


class Rarity(Enum):
    Common = 1
    Uncommon = 2
    Rare = 3
    Epic = 4
    Legendary = 5
    Mystical = 6
    Godlike = 7


class BaseItem:
    def __init__(self):
        self.name: str = 'baseitem'
        self.rarity: Rarity = Rarity.Godlike
        self.context_menu: ItemContextMenu = ItemContextMenu(self)

    def get_name(self) -> str:
        return Locale.get(self.name)

    def get_description(self) -> str:
        return Locale.get(self.name + '_desc')

    def __str__(self):
        return self.get_name()
