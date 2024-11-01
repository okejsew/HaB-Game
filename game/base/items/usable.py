from game.localization import Locale
from game.base.item import BaseItem, ItemContextMenu
from tui.elements.button import Button


class UsableContextMenu(ItemContextMenu):
    def __init__(self, item: 'Usable'):
        super().__init__(item)
        self.add(Button(Locale.get("use"), item.use))


class Usable(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'usable'
        self.context_menu = UsableContextMenu(self)

        self.usages: int = 0
        self.max_usages: int = 100

    def use(self): ...

    def __str__(self):
        return f'[{self.usages} / {self.max_usages}] {self.get_name()}'
