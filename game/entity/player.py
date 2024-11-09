from game.entity import BaseEntity


class Player(BaseEntity):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Player, cls).__new__(cls)
        return cls._instance

    def __init__(self, name: str = 'Игрок'):
        super().__init__()
        self.name: str = name
