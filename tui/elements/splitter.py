from tui import BaseElement


class Splitter(BaseElement):
    def __init__(self):
        super().__init__()
        self.len: int = 10

    def __str__(self):
        return '-' * self.len
