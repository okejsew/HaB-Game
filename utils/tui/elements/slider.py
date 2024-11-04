from utils.tui import BaseElement


class Slider(BaseElement):
    def __init__(self):
        super().__init__()
        self.focus = True
        self.value: int = 0
        self.percents: bool = True

    def on_key(self, key: int):
        if key == 261:
            self.value = min(self.value + 1, 10)
        elif key == 260:
            self.value = max(self.value - 1, 0)

    def __str__(self):
        string = f'[{"#" * self.value + " " * (10 - self.value)}]'
        string += f' {self.value * 10}/100 %' if self.percents else ''
        return string
