from enum import Enum
from typing import Optional, Callable

from tui import BaseElement


class ButtonStyle(Enum):
    Square = 1
    Cursor = 2
    Cell = 3


class Button(BaseElement):
    def __init__(self, text: str = 'Button', click: Optional[Callable] = None, style: ButtonStyle = ButtonStyle.Square):
        super().__init__()
        self.text: str = text
        self.focus = True
        self.click: Optional[Callable] = click
        self.style: ButtonStyle = style

    def on_click(self):
        if self.click: self.click()

    def __str__(self):
        match self.style:
            case ButtonStyle.Square:
                return f'[{self.text}]'
            case ButtonStyle.Cell:
                return f'# {self.text}'
            case ButtonStyle.Cursor:
                return f'> {self.text}'
