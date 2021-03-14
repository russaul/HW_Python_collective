import tkinter as tk
import random
import datetime

lst = []
for i in range(1, 17):
    lst.append(i)
random.shuffle(lst)


window = tk.Tk()
window.columnconfigure(0, weight = 1, minsize = 1)
window.rowconfigure(0, weight = 1, minsize = 1)
window.rowconfigure(1, weight = 200, minsize = 1)
frame_up = tk.Frame(master = window)

frame_up.grid(row = 0, column = 0, sticky = "we")

for i in range(2):
    frame_up.columnconfigure(i, weight = 1, minsize = 1)
    frame_up.rowconfigure(0, weight = 1, minsize = 1)

frame_new = tk.Button(
    master = frame_up,
    relief = tk.RAISED,
    borderwidth = 2,
    text = "new"
)
frame_new.grid(row = 0, column = 0, sticky = "w")

frame_exit = tk.Button(
    master = frame_up,
    relief = tk.RAISED,
    borderwidth = 2, 
    text = "exit"
)
frame_exit.grid(row = 0, column = 1, sticky = "e")

frame_down = tk.Frame(master = window)
frame_down.grid(row = 1, column = 0, sticky = "nsew")

#Cells with numbers
for i in range(4):
    frame_down.columnconfigure(i, weight = 1, minsize = 1)
    frame_down.rowconfigure(i, weight = 1, minsize = 1)
    for j in range(4):
        frame = tk.Button(
            master = frame_down,
            relief = tk.RAISED,
            borderwidth = 5,
            text = "1"
        )
        frame.grid(row = i, column = j, sticky="nsew")

window.mainloop()
