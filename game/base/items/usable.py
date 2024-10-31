from game.base.item import BaseItem


class Usable(BaseItem):
    def __init__(self):
        super().__init__()
        self.usages: int = 0
        self.max_usages: int = 100

    def on_usage(self): ...

    def __str__(self):
        return f'{self.name} [{self.usages} / {self.max_usages}]'
