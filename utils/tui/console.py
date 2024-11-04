import curses

import _curses

window: _curses.window = curses.initscr()
window.border(0)
curses.cbreak()
curses.noecho()
window.keypad(True)
curses.curs_set(0)
curses.start_color()
curses.mousemask(curses.REPORT_MOUSE_POSITION)
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)


def color(color_num: int):
    return curses.color_pair(color_num)
