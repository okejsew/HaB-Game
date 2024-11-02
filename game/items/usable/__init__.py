from game.base.item import BaseItem
from game.items.usable.menu import UsableContextMenu


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
