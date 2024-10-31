from tui import BaseElement


class Checkbox(BaseElement):
    def __init__(self):
        super().__init__()
        self.text: str = 'Checkbox'
        self.focus = True
        self.checked: bool = False

    def on_click(self):
        self.checked = not self.checked

    def __str__(self):
        return f'[{"*" if self.checked else " "}] {self.text}'
