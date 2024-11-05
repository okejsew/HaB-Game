import time

from localization import Locale
from utils.tui import window


class Dialog:
    def __init__(self):
        self.phrases: list[str] = []
        self.rules: dict[str, float | int] = {'!': 0.4, '.': 0.4, '?': 0.4, ',': 0.2}

    def show(self):
        window.clear()
        for phrase in self.phrases:
            for s in phrase:
                window.addch(s)
                window.refresh()
                time.sleep(0.02)
                if s in self.rules.keys():
                    time.sleep(self.rules[s])
            window.getch()
