import curses
# For Windows:
# pip install windows-curses
# For Linux and MacOS:
# pip install curses

def main(stdscr):
    curses.curs_set(0)  # Скрыть курсор
    stdscr.nodelay(1)   # Не блокировать при ожидании ввода
    stdscr.timeout(100) # Таймаут ожидания ввода

    while True:
        key = stdscr.getch()

        if key == curses.KEY_LEFT:
            stdscr.addstr(10, 0, "Left arrow key pressed   ")
        elif key == curses.KEY_RIGHT:
            stdscr.addstr(10, 0, "Right arrow key pressed  ")
        elif key == ord('q') or key == 27:
            break

        stdscr.refresh()

if __name__ == "__main__":
    curses.wrapper(main)