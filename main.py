import curses
import atexit
from button import Button

# init curses screen
screen = curses.initscr()

# cleanup
def exit():
    curses.setupterm()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
atexit.register(exit)

# init curses
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
curses.mousemask(1)

def q():
    quit()

b = Button(screen, "test", q, 1, 1, 15)
def draw():
    b.draw()
    screen.refresh()

def uppdate():
    ch = screen.getch()
    if ch == curses.KEY_MOUSE:
        (_,x,y,_,_) = curses.getmouse()
        b.uppdate(x,y)

def main():
    height, width = screen.getmaxyx()
    while True:
        draw()
        uppdate()

    screen.touchwin()
    screen.refresh()

main()
