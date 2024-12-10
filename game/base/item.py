from game.base.object import Object


class Item(Object):
    def __init__(self, name: str = 'Item'):
        super().__init__(name)
        
        from game.base.entity import Entity
        self.owner: Entity | None = None
