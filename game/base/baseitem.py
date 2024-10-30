class BaseItem:
    def __init__(self):
        self.name: str = 'BaseItem'


class Weapon(BaseItem):
    def __init__(self):
        super().__init__()


class Armor(BaseItem):
    def __init__(self):
        super().__init__()


class Interactable(BaseItem):
    def __init__(self):
        super().__init__()
