class Button:
    def __init__(self, screen, txt, func, x, y, width = 0, marg = 1, bord = 1, pad = 1, short = 3, marger = " ", border = "*", pader = " ", shorter = ".", bottom = True):
        self._screen = screen
        self._txt = txt
        self._func = func
        self._x = x
        self._y = y
        self._extra = marg * 2 + bord * 2 + pad * 2
        self._min = self._extra + short
        if width == 0:
            self._width = self._extra + len(txt)
        else:
            if width < self._min:
                self._width = self._min
            else:
                self._width = width
        self._height = self._extra + 1
        self._marg = marg
        self._bord = bord
        self._pad = pad
        self._short = short
        self._marger = marger
        self._border = border
        self._pader = pader
        self._shorter = shorter
        self._bottom = bottom

    def uppdate(self, x, y, usr = None):
        if (x >= self._x and x <= (self._x + self._width) and
                y >= self._y and y <= (self._y + self._height)):
            if usr == None:
                self._func()
            else:
                self._func(usr)

    def propper(self, num = False):
        prop = len(self._txt) + self._extra
        if num:
            return prop
        if (self._width >= prop):
            return True
        return False

    def prt(self, times, text, x, y):
        for i in range(times):
            self._screen.addstr(y, x, str(text))
            y = y + 1
        return y

    def under(self):
        ret = self._y + self._extra + 1
        if not self._bottom:
            ret -= 1
        return ret

    def nextPropper(self):
        return self._x + self._width

    def width(self, width=None, propper=False):
        if width == None and not propper:
            return self._width
        else:
            if propper:
                if width != None:
                    self._width = width
                if not self.propper():
                    self._width = self._extra + len(self._txt)
            else:
                if width < self._min:
                    self._width = self._min
                else:
                    self._width = width

    def height(self):
        if self._bottom:
            return self._extra + 1
        return self._extra

    def draw(self):
        leng = self._width
        text = self._txt
        if len(text) > leng - self._extra:
            text = text[:leng - self._extra - self._short] + self._shorter * self._short
        text = text + self._pader * (leng - self._extra - len(text))

        marg = self._marger * self._marg
        bord = self._border * self._bord
        pad = self._pader * self._pad
        mar = self._marger * leng
        bor = marg + self._border * (leng - self._marg * 2) + marg
        pa = marg + bord + self._pader * (leng - self._marg * 2 - self._bord * 2) + bord + marg
        txt = marg + bord + pad + text + pad + bord + marg

        y = self.prt(self._marg, mar, self._x, self._y)
        y = self.prt(self._bord, bor, self._x, y)
        y = self.prt(self._pad, pa, self._x, y)
        y = self.prt(1, txt, self._x, y)
        y = self.prt(self._pad, pa, self._x, y)
        y = self.prt(self._bord, bor, self._x, y)
        if self._bottom:
            y = self.prt(self._marg -1, mar, self._x, y)
