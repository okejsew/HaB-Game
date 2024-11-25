from game.item import BaseItem


class BattleItem(BaseItem):
    def __init__(self):
        super().__init__()

        self.durability = 50
        self.max_durability = 50
        self.factor = 1
