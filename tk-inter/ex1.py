import tkinter as tk

fenetre = tk.Tk()

tk.Button(fenetre, text="A").grid(column=0, row=0)
tk.Button(fenetre, text="B").grid(column=1, row=0)
tk.Button(fenetre, text="C").grid(column=2, row=0)
tk.Button(fenetre, text="D").grid(column=0, row=1)
tk.Button(fenetre, text="E").grid(column=1, row=2, columnspan=2, sticky=tk.EW)

fenetre.mainloop()