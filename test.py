import curses

from game.utils.tui import *

tui = Tui()

def ex():
    tui.showing = False
    curses.endwin()
    exit()

tui.add(Label())
tui.add(Splitter())
tui.add(Button())
tui.add(Checkbox())
tui.add(ProgressBar())
b = Button()
b.text = 'Exit'
b.click = ex
tui.add(b)

tui.show()