from game.core.guid import GUID
from game.core.settings import Settings


class Object:
    def __init__(self, name: str = 'Object'):
        self.name = name
        self.guid: GUID = GUID()
        GUID.objects[self.guid] = self

    def __repr__(self):
        string = f'{self.__class__.__name__}'.ljust(Settings.ljust_guid)
        string += f'[{self.guid}]["{self.name}"]'.ljust(Settings.ljust_name)
        return string
