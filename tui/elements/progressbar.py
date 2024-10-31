from tui import BaseElement


class ProgressBar(BaseElement):
    def __init__(self):
        super().__init__()
        self.focus = True
        self.value: int = 0
        self.percents: bool = True

    def __str__(self):
        string = f'[{"#" * self.value + " " * (10 - self.value)}]'
        string += f' {self.value * 10}/100 %' if self.percents else ''
        return string
