import curses
from curses import wrapper


def start_screen(std_scr):
    std_scr.clear()
    std_scr.addstr(0, 0, "Welcome to the Speed Typing Test")
    std_scr.addstr("\nPress any key to begin!")
    std_scr.refresh()
    std_scr.getkey()


def display_text(std_scr, target, current, wpm=0):
    std_scr.addstr(target)
    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            pass
        std_scr.addstr(0, i, char, )


def wpm_test(std_scr):
    target_text = "Hello World this is some test text for this app!"
    current_text = []
    while True:
        std_scr.clear()
        display_text(std_scr, target_text, current_text)
        std_scr.refresh()

        key = std_scr.getkey()
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)


def main(std_scr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_WHITE)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    start_screen(std_scr)
    wpm_test(std_scr)


wrapper(main)
