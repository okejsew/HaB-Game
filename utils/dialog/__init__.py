import time

from localization import Locale
from utils.tui import window


class Dialog:
    def __init__(self):
        self.phrases: list[str] = []
        self.rules: dict[str, float | int] = {'!': 0.4, '.': 0.4, '?': 0.4, ',': 0.2}

    def start(self):
        window.clear()
        for phrase in self.phrases:
            for s in phrase:
                window.addch(s)
                window.refresh()
                time.sleep(0.02)
                if s in self.rules.keys():
                    time.sleep(self.rules[s])
            window.getch()

class DialogFabric:
    @staticmethod
    def load(name: str):
        dialog = Dialog()
        with open(f'resources/dialogs/{name}.dg', 'r', encoding='utf-8') as file:
            for line in file.readlines():
                if line.strip():
                    if line.startswith('#'):
                        char, t = line.lstrip('#').split(':')
                        dialog.rules[char.strip()] = float(t)
                    elif line.startswith('@'):
                        dialog.phrases.append(Locale.get(line.lstrip('@')))
                    else:
                        dialog.phrases.append(line.strip() + '\n')
        return dialog

