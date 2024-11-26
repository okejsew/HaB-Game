from typing import TYPE_CHECKING, Optional

from game.core.object import Object

if TYPE_CHECKING:
    from game.base.entity import Entity


class Item(Object):
    def __init__(self, name: str = 'Item'):
        super().__init__(name)
        self.owner: Optional['Entity'] = None
