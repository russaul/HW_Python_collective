import tkinter as tk
import random
import datetime


def new_game():
    lst = list(range(1,16))
    random.shuffle(lst)
    frame_down = tk.Frame()
    frame_down.grid(row = 1, column = 0, sticky = "nsew")
    t = 0
    buttons = []
    global empty 
    empty = 0
    for i in range(4):
        frame_down.columnconfigure(i, weight = 1, minsize = 10)
        frame_down.rowconfigure(i, weight = 1, minsize = 10)
        for j in range(4):
            if t == 15:
                break
            frame = tk.Button(
                master = frame_down,
                relief = tk.RAISED,
                borderwidth = 5,
                text = f"{lst[t]}",
                command = lambda x=lst[t]: move(x, lst, buttons)
            )
            buttons.append(frame)
            t += 1
            frame.grid(row = t//4+1, column = t%4, sticky="nsew")


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
        buttons[cur_ind].grid(row=new_row, column=new_column, sticky="SEWN")
        empty = (start_row-1)*4 + start_column
        if check(buttons):
            messagebox.showinfo(title="Win message", message="You win!")
            new_game()


def check(buttons):
    global empty
    if empty != 15:
        return False
    for i in range(15):
        cur_row = buttons[i].grid_info()["row"]
        cur_column = buttons[i].grid_info()["column"]
        if ((cur_row - 1) * 4 + cur_column) != i:
            return False
    return True


#Drawing window and field
window = tk.Tk()

frame_up = tk.Frame(master = window)
frame_new = tk.Button(
    master = frame_up,
    relief = tk.RAISED,
    borderwidth = 2,
    text = "new",
    command = new_game
)

frame_exit = tk.Button(
    master = frame_up,
    relief = tk.RAISED,
    borderwidth = 2, 
    text = "exit",
    command = fin
)

window.columnconfigure(0, weight = 1, minsize = 2)
window.rowconfigure(0, weight = 1, minsize = 2)
window.rowconfigure(1, weight = 200, minsize = 2)
for i in range(2):
    frame_up.columnconfigure(i, weight = 1, minsize = 2)
    frame_up.rowconfigure(0, weight = 1, minsize = 2)

frame_up.grid(row = 0, column = 0, sticky = "we")
frame_new.grid(row = 0, column = 0, sticky = "w")
frame_exit.grid(row = 0, column = 1, sticky = "e")

new_game()

window.mainloop()