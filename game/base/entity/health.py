from game.base.item import BodyPart


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

    def heal(self, amount: int, bodypart: BodyPart):
        setattr(self, bodypart.name, min(getattr(self, bodypart.name + '_max'), getattr(self, bodypart.name) + amount))

    def damage(self, amount: int, bodypart: BodyPart):
        setattr(self, bodypart.name, max(0, getattr(self, bodypart.name) - amount))