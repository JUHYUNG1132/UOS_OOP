from tkinter import *
key = 0

def keyB(e):
    global key
    key = e.keysym
    print(key)
    
tk = Tk()
tk.bind('<Key>', keyB)
tk.mainloop()