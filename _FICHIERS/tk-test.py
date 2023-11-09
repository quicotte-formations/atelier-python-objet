import tkinter as tk

class App(tk.Tk):
    def clic(self,e:tk.Event):
        print( e.widget.verso )

    def __init__(self):
        super().__init__()

        self.minsize(800,600)

        for i in range(10):
            for j in range(10):

                b = tk.Button( self, text = "?")
                b.verso = i+j
                b.bind('<Button-1>', self.clic)
                b.grid(row=i,column=j)


        self.mainloop()

app = App()