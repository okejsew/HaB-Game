from game.entity import BaseEntity


class Player(BaseEntity):
    def __init__(self, name: str = 'Игрок'):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"""Здоровье - {self.health}
Инвентарь - {self.inventory}
Снаряжение - {self.equipment}"""
