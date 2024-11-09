from game.item import BaseItem


class Health:
    def __init__(self):
        self.head: int = 0
        self.hands: int = 0
        self.chest: int = 0
        self.legs: int = 0
        self.feet: int = 0

        self.head_max: int = 100
        self.hands_max: int = 100
        self.chest_max: int = 100
        self.legs_max: int = 100
        self.feet_max: int = 100


class BaseEntity:
    def __init__(self):
        self.name: str = 'Сущность'
        self.health: Health = Health()
        self.inventory: list[BaseItem] = []
