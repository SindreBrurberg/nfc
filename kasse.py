import curses
import atexit
from button import Button
import RPi.GPIO as GPIO
import MFRC522

# init curses screen
screen = curses.initscr()

# cleanup
def exit():
    global continue_reading
    curses.setupterm()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    continue_reading = False
    GPIO.cleanup()
atexit.register(exit)

# init curses
curses.noecho()
curses.curs_set(0)
screen.keypad(1)
curses.mousemask(1)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

#Usefull base variables
width, heigth = screen.getmaxyx()
screens = [screen]

#User info
#Creating usr screen
usrscr = curses.newwin(5, width, 0, 0)
screens.append(usrscr)

def fetchUser(uid):
    if uid != None:
        return {"name":"Sindre S Brurberg", "polser":2, "vafler":2, "brus":6, "mat":0}
    return None

def useBong(usr, bong):
    if usr[bong] > 0:
        usr[bong] -= 1
        return (usr, True)
    return (usr, False)

def drawUsr(scr, usr):
    scr.addstr(0,0, usr[name])

#Button part
def genButtonFunc(bong):
    def bFunc(usr):
        useBong(usr, bong)


#Initing button screen
buttonWin = curses.newwin(15, width, 5, 0)
screens.append(buttonWin)

#Initing buttons
polser = Button(buttonWin, "polser", genButtonFunc("polser"), 0, 0)
vafler = Button(buttonWin, "vafler", genButtonFunc("vafler"), polser.nextPropper(), 0, bottom = False)
brus = Button(buttonWin, "brus", genButtonFunc("brus"), polser.nextPropper(), polser.under(), width = vafler.width(), bottom = False)
mat = Button(buttonWin, "mat", genButtonFunc("mat"), 0, polser.under(), width=polser.width(), bottom = False)

#Adding buttons to button "bus"
buttns = [polser, vafler, brus, mat]

user = None
def draw():
    if user != None:
        drawUsr(usrscr, user)
    for b in buttns:
        b.draw()
    for s in screens:
        s.refresh()

def uppdate():
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:
        user = fetchUser(uid)

    # Use button
    ch = screen.getch()
    if ch == curses.KEY_MOUSE:
        (_,x,y,_,_) = curses.getmouse()
        for b in buttns:
            b.uppdate(x,y, user)

def main():
    height, width = screen.getmaxyx()
    while True:
        draw()
        uppdate()

    screen.touchwin()
    screen.refresh()

main()
