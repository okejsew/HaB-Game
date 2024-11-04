import time

from tui import window


class Phrase:
    def __init__(self, text: str, char_time: float = 0.05):
        self.text: str = text
        self.char_time: float = char_time

class Dialog:
    def __init__(self):
        self.phrases: list[Phrase] = []

    def load(self):
        pass

    def start(self):
        window.clear()
        for phrase in self.phrases:
            for s in phrase.text:
                window.addch(s)
                window.refresh()
                time.sleep(phrase.char_time)
                if s in ['!', '.', '?', ',']:
                    time.sleep(0.2)
            window.getch()