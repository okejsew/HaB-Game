from typing import Optional
from uuid import UUID


class Object:
    def __init__(self, name: str = 'Object'):
        self.id: Optional[UUID] = None
        self.name = name