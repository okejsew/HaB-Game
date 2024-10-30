import curses
from typing import Callable, Optional, TypeVar, Type
import re

from game.utils.console import window
from game.utils.localization import Locale

tuis: list['Tui'] = []
T = TypeVar('T')

class BaseElement:
    def __init__(self):
        self.name: str = 'BaseElement'
        self.focus: bool = False

    def on_click(self): ...

    def on_key(self, key: int): ...

    def __str__(self):
        return 'BaseElement'


class Button(BaseElement):
    def __init__(self, text: str = 'Button', click: Optional[Callable] = None):
        super().__init__()
        self.text: str = text
        self.focus = True
        self.click: Optional[Callable] = click

    def on_click(self):
        if self.click: self.click()

    def __str__(self):
        return f'[{self.text}]'


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


class Slider(BaseElement):
    def __init__(self):
        super().__init__()
        self.focus = True
        self.value: int = 0
        self.percents: bool = True

    def on_key(self, key: int):
        if key == curses.KEY_RIGHT:
            self.value = min(self.value + 1, 10)
        elif key == curses.KEY_LEFT:
            self.value = max(self.value - 1, 0)

    def __str__(self):
        string = f'[{"#" * self.value + " " * (10 - self.value)}]'
        string += f' {self.value * 10}/100 %' if self.percents else ''
        return string

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


class Splitter(BaseElement):
    def __init__(self):
        super().__init__()
        self.len: int = 10

    def __str__(self):
        return '-' * self.len


class Label(BaseElement):
    def __init__(self, text: str = 'Label'):
        super().__init__()
        self.text = text

    def __str__(self):
        return self.text


class Tui:
    def __init__(self):
        self.elements: list[BaseElement] = []
        self.showing: bool = False
        self.index = 0
        tuis.append(self)

    def add(self, element: BaseElement):
        self.elements.append(element)

    def close(self):
        self.showing = False

    def next(self, tui: 'Tui'):
        self.close()
        tui.show()

    def get(self, name: str, t: Type[T]) -> Optional[T]:
        for element in self.elements:
            if isinstance(element, t) and name == element.name:
                return element

    def show(self):
        self.showing = True
        _, y = window.getmaxyx()
        while self.showing:
            window.clear()
            focusable_elems = [elem for elem in self.elements if elem.focus]

            for i, element in enumerate(self.elements[:y]):
                color_num = 2 if focusable_elems and element is focusable_elems[self.index] else 1
                window.addstr(i, 0, str(element), curses.color_pair(color_num))

            key = window.getch()
            if key == curses.KEY_UP:
                self.index = max(self.index - 1, 0)
            elif key == curses.KEY_DOWN:
                self.index = min(self.index + 1, len(focusable_elems) - 1)
            elif key == ord('\n'):
                if focusable_elems:
                    focusable_elems[self.index].on_click()
            else:
                if focusable_elems:
                    focusable_elems[self.index].on_key(key)

    def load(self, path: str):
        current_element = None
        element_pattern = re.compile(r'(\w+):')
        attr_pattern = re.compile(r'(\w+)\s*=\s*(.+)')

        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()

                element_match = element_pattern.match(line)
                if element_match:
                    element_type = element_match.group(1)

                    if element_type in globals() and issubclass(globals()[element_type], BaseElement):
                        current_element = globals()[element_type]()
                        self.add(current_element)
                    continue

                attr_match = attr_pattern.match(line)
                if attr_match and current_element:
                    attr_name, attr_value = attr_match.groups()

                    if attr_value.startswith("'") and attr_value.endswith("'"):
                        attr_value = attr_value[1:-1]
                        if attr_value.startswith('@'):
                            attr_value = Locale.get(attr_value.strip('@'))
                    elif attr_value.isdigit():
                        attr_value = int(attr_value)
                    elif attr_value in ['True', 'False']:
                        attr_value = attr_value == 'True'

                    setattr(current_element, attr_name, attr_value)

    @staticmethod
    def end():
        for tui in tuis:
            tui.close()

