class Rarity:
    common = 1
    uncommon = 2
    rare = 3
    epic = 4
    legendary = 5
    Mystical = 6
    Godlike = 7

class BaseItem:
    def __init__(self):
        self.name: str = 'BaseItem'
        self.rarity: int = Rarity.common


class Weapon(BaseItem):
    def __init__(self):
        super().__init__()


class Armor(BaseItem):
    def __init__(self):
        super().__init__()


class Interactable(BaseItem):
    def __init__(self):
        super().__init__()
