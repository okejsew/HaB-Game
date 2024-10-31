from game.entity import BaseEntity


class Player(BaseEntity):
    def __init__(self):
        super().__init__()
        self.name: str = 'Player'
