from game.base.baseitem import BaseItem


class Inventory:
    def __init__(self):
        self.items: list[BaseItem] = []

    def show(self):
        ...