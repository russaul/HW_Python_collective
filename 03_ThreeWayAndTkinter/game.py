import tkinter as tk
import random
from tkinter import messagebox


def new_game():
    lst = list(range(1,16))
    random.shuffle(lst)
    frame_down = tk.Frame(master = window, bg = "gray20")
    frame_down.grid(row = 1, column = 0, sticky = "nsew")
    t = 0
    buttons = []
    global empty 
    empty = 15
    for i in range(4):
        frame_down.columnconfigure(i, weight = 1, minsize = 1)
        frame_down.rowconfigure(i+1, weight = 1, minsize = 1)
        for j in range(4):
            if t == 15:
                break
            frame = tk.Button(
                master = frame_down,
                relief = tk.RAISED,
                borderwidth = 5,
                width=4,
                height=2,
                fg = "LightBlue1",
                bg = "MediumPurple4",
                text = f"{lst[t]}",
                command = lambda x=lst[t]: move(x, lst, buttons)
            )
            buttons.append(frame)
            frame.grid(row = t//4+1, column = t%4, sticky="nsew")
            t += 1


def fin():
    exit(0)


def move(x, lst, buttons):
    global empty
    cur_ind = lst.index(x)
    start_row = buttons[cur_ind].grid_info()['row']
    start_column = buttons[cur_ind].grid_info()['column']
    new_row = empty//4+1
    new_column = empty%4
    if ((abs(new_row-start_row) == 1) and (new_column == start_column)) or ((abs(new_column-start_column) == 1) and (new_row == start_row)):
        buttons[cur_ind].grid(row=new_row, column=new_column, sticky="nsew")
        empty = (start_row-1)*4 + start_column
        if check(buttons):
            messagebox.showinfo(title="Win message", message="You win!")
            new_game()


def check(buttons):
    global empty
    result = 0
    for i in range(15):
        cell_position = (buttons[i].grid_info()['row'] - 1) * 4 + buttons[i].grid_info()['column']
        result += int(str(cell_position+1) == buttons[i].cget('text'))
    if result == 15: 
        messagebox.showinfo('', 'You win!')
        new_game()


#Drawing window and field
window = tk.Tk()

frame_up = tk.Frame(master = window, bg = "gray15")
frame_new = tk.Button(
    master = frame_up,
    relief = tk.RAISED,
    borderwidth = 2,
    text = "new",
    bg = "purple4",
    command = new_game
)

frame_exit = tk.Button(
    master = frame_up,
    relief = tk.RAISED,
    borderwidth = 2, 
    text = "exit",
    bg = "purple4",
    command = fin
)

window.columnconfigure(0, weight = 1, minsize = 1)
window.rowconfigure(0, weight = 1, minsize = 1)
window.rowconfigure(1, weight = 200, minsize = 1)
for i in range(2):
    frame_up.columnconfigure(i, weight = 1, minsize = 1)
    frame_up.rowconfigure(0, weight = 1, minsize = 1)

frame_up.grid(row = 0, column = 0, sticky = "we")
frame_new.grid(row = 0, column = 0, sticky = "w")
frame_exit.grid(row = 0, column = 1, sticky = "e")

new_game()

window.mainloop()