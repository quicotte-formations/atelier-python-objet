import tkinter as tk

def calculer_imc():
    resultat = poids.get() / ((taille_en_cm.get()/100)**2)

    # Affiche imc
    imc.set( f'IMG: {resultat}' )

    # Affiche diagnostic
    diag = ''
    if resultat<16.5:
        diag='dénutrition'
    elif resultat<=17.5:
        diag='maigreur'
    elif resultat<=25:
        diag='poids normal'
    elif resultat <= 30:
        diag = 'surpoids'
    elif resultat<=35:
        diag='obésité modérée'
    elif resultat<=40:
        diag='obésité sévère'
    else:
        diag='obésité massive'

    diagnostic.set(diag)


fenetre = tk.Tk()

# Définit variables associées aux widgets

taille_en_cm = tk.IntVar()
poids = tk.IntVar()
imc = tk.StringVar()
imc.set('A DETERMINER')
diagnostic = tk.StringVar()
diagnostic.set('A DETERMINER')

# Définit widgets
tk.Label(fenetre, text='Taille').grid(row=0, column=0,pady=30, padx=30)
tk.Entry(fenetre, textvariable=taille_en_cm).grid(row=0, column=1, columnspan=2)
tk.Label(fenetre, text='Poids').grid(row=1, column=0)
tk.Entry(fenetre, textvariable=poids).grid(row=1, column=1, columnspan=2)
tk.Button(fenetre, text='Calculer !', command=calculer_imc ).grid(row=2, column=0, columnspan=3, sticky=tk.EW)
tk.Label(fenetre, textvariable=imc).grid(row=3, column=0, columnspan=3)
tk.Label(fenetre, textvariable=diagnostic).grid(row=4, column=0, columnspan=3)

fenetre.mainloop()