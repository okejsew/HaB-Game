from typing import TYPE_CHECKING, TypeVar, Type, Optional

if TYPE_CHECKING:
    from game.core.object import Object

T = TypeVar('T')


class GUID:
    id: int = 0
    objects: dict['GUID', 'Object'] = {}

    @staticmethod
    def get_new() -> int:
        GUID.id += 1
        return GUID.id

    @staticmethod
    def get(t: Type[T], guid: 'GUID') -> Optional[T]:
        if isinstance(obj := GUID.objects[guid], t):
            return obj

    def __init__(self):
        self.id = self.get_new()

    @staticmethod
    def info():
        for obj in GUID.objects.values():
            print(obj)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: 'GUID'):
        return self.id == other.id

    def __repr__(self):
        return f'GUID={self.id}'
