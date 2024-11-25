from game.item.armor import BodyPart


class Health:
    def __init__(self):
        self.head: int = 30
        self.hands: int = 20
        self.chest: int = 50
        self.legs: int = 20
        self.feet: int = 10

        self.head_max: int = 30
        self.hands_max: int = 20
        self.chest_max: int = 50
        self.legs_max: int = 20
        self.feet_max: int = 10

    def change(self, hp: int, bodypart: BodyPart):
        new_hp = min(getattr(self, f'{bodypart.name}_max'), max(0, getattr(self, bodypart.name) + hp))
        setattr(self, bodypart.name, new_hp)

    def __str__(self):
        return f"""
    Голова  - {self.head} / {self.head_max}
    Руки    - {self.hands} / {self.hands_max}
    Тело    - {self.chest} / {self.chest_max}
    Ноги    - {self.legs} / {self.legs_max}
    Ступни  - {self.feet} / {self.feet_max}"""
