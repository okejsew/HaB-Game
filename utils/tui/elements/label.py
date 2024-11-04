from utils.tui import BaseElement


class Label(BaseElement):
    def __init__(self, text: str = 'Label'):
        super().__init__()
        self.text = text

    def __str__(self):
        return self.text
