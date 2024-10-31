class BaseElement:
    def __init__(self):
        self.name: str = 'BaseElement'
        self.focus: bool = False

    def on_click(self): ...

    def on_key(self, key: int): ...

    def __str__(self):
        return 'BaseElement'
