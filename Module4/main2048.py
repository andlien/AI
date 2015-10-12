from visuals import GameWindow
from Tkinter import *
import time

teller = 0

root = Tk()
#root.geometry("250x150+300+300")
#app = GameWindow()


#frame = Frame(width=768, height=576, bg="", colormap="new")
window = GameWindow()
board = [   # A list of values currently present in the board on the form 2^x.
            # Eg: the number 4 implies that the graphical board should display,
            # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
            0, 2, 4, 4,
            0, 2, 1, 3,
            0, 1, 1, 3,
            0, 0, 2, 1
        ]

window.update_view( board ) # 1D list representing the board


def hei():
    global teller
    teller += 2
    board = [   # A list of values currently present in the board on the form 2^x.
            # Eg: the number 4 implies that the graphical board should display,
            # 2^4 = 16, the digit 16. This board represents the board in the screen dump below.
            0, 2, 4, 4,
            teller, 2, 1, 3,
            0, 1, 1, 3,
            teller, 0, 2, 1
        ]
    window.update_view( board )
    window.after(2000,hei)
    #time.sleep(2)


window.after(2000,hei)

root.mainloop()
print("Hei")

