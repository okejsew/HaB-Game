from game.core.guid import GUID


class Object:
    def __init__(self, name: str = 'Object'):
        self.name = name
        self.guid: GUID = GUID()

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.guid}]["{self.name}"]'
