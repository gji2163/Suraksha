from tkinter import *
from keyboard import add_hotkey

def Q():
    global var
    var = (var+1)%2
    
add_hotkey('Esc',Q)
var = 0

while True:
    m=Tk()
    m['bg']='black'
    m.config(cursor="none")
    m.attributes("-fullscreen", True)
    m.attributes('-topmost', True)

    m.mainloop()
    if var:
        break
