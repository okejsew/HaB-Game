from game.entity import BaseEntity


class Enemy(BaseEntity):
    def __init__(self):
        super().__init__()
        self.name: str = 'Противник'
