import tkinter as tk

class InputLabel(tk.Label):
    def __init__(self, master = None):
        tk.Label.__init__(self, master)
        self.grid(sticky = tk.N + tk.S + tk.E + tk.W)



app = InputLabel()
app.mater.title("Editor")
app.mainloop()