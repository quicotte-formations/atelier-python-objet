import tkinter as tk

def clic(e:tk.Event):
    print( e.widget.cle )

fenetre = tk.Tk()

a = tk.Button(fenetre, text="A")
a.grid(column=0, row=0)
b = tk.Button(fenetre, text="B")
b.grid(column=1, row=0)
tk.Button(fenetre, text="C").grid(column=2, row=0)
tk.Button(fenetre, text="D").grid(column=0, row=1)
tk.Button(fenetre, text="E").grid(column=1, row=2, columnspan=2, sticky=tk.EW)

a.cle = 123
b.cle = 456
a.bind('<Enter>', clic)
b.bind('<Enter>', clic)

fenetre.mainloop()