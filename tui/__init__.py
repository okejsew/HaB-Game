from typing import TypeVar, Type, Optional, Callable

from tui.console import window, color
from tui.element import BaseElement

tuis: list['Tui'] = []
T = TypeVar('T')


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

    def next(self, tui: Callable):
        self.close()
        tui()

    def get(self, name: str, t: Type[T]) -> Optional[T]:
        for element in self.elements:
            if type(element).__name__ == t.__name__ and name == element.name:
                return element

    def show(self):
        self.showing = True
        _, y = window.getmaxyx()
        while self.showing:
            window.clear()
            focusable_elems = [elem for elem in self.elements if elem.focus]

            for i, element in enumerate(self.elements[:y]):
                color_num = 2 if focusable_elems and element is focusable_elems[self.index] else 1
                window.addstr(i, 0, str(element), color(color_num))

            key = window.getch()
            if key == 259:
                self.index = max(self.index - 1, 0)
            elif key == 258:
                self.index = min(self.index + 1, len(focusable_elems) - 1)
            elif key == ord('\n'):
                if focusable_elems:
                    focusable_elems[self.index].on_click()
            else:
                if focusable_elems:
                    focusable_elems[self.index].on_key(key)

    @staticmethod
    def end():
        for tui in tuis:
            tui.close()
