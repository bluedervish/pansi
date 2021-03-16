from curses import wrapper, curs_set

values = []


class Screen(object):

    def __init__(self, screen):
        self._screen = screen

    def clear(self):
        self._screen.clear()


def main(stdscr):
    stdscr.clear()
    max_y, max_x = stdscr.getmaxyx()
    stdscr.addch(max_y - 1, max_x - 2, '▀')
    stdscr.refresh()
    stdscr.getkey()
    values.append(stdscr.inch(0, 0))


if __name__ == "__main__":
    curs_set(0)
    wrapper(main)
