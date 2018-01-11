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

width, heigth = screen.getmaxyx()

def polserf():
    quit()

buttonWin = curses.newwin(15, width, 5, 0)
polser = Button(buttonWin, "polser", polserf, 0, 0)
vafler = Button(buttonWin, "vafler", polserf, polser.nextPropper(), 0, bottom = False)
brus = Button(buttonWin, "brus", polserf, polser.nextPropper(), polser.under(), width = vafler.width(), bottom = False)
mat = Button(buttonWin, "mat", polserf, 0, polser.under(), width=polser.width(), bottom = False)
buttns = [polser, vafler, brus, mat]
screens = [screen, buttonWin]

def userInfo():
    return ("Sindre Brurberg", 2, 2, 6, 0)

def draw():
    for b in buttns:
        b.draw()
    for s in screens:
        s.refresh()

def uppdate():
    ch = screen.getch()
    if ch == curses.KEY_MOUSE:
        (_,x,y,_,_) = curses.getmouse()
        for b in buttns:
            b.uppdate(x,y)

def main():
    height, width = screen.getmaxyx()
    while True:
        draw()
        uppdate()

    screen.touchwin()
    screen.refresh()

main()
