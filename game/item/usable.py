from game.item import BaseItem


class Usable(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'Используемое'

        self.usages: int = 0
        self.max_usages: int = 100

    def __str__(self):
        return f'[{self.usages} / {self.max_usages}] {self.name}'
