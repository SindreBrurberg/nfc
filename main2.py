from button import Button

def q():
    pass

b = Button("screen", "test", q, 1, 1, 15)
def draw():
    b.draw()

def uppdate():
    b.uppdate(x,y)

def main():
    while True:
        draw()
        uppdate()
