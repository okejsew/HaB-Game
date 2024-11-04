from typing import TYPE_CHECKING
from localization import Locale
from utils.tui import BaseElement
from utils.tui.elements.label import Label
from utils.tui.elements.splitter import Splitter

if TYPE_CHECKING:
    from game.base.item import BaseItem

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


