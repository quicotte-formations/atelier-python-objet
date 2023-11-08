import turtle

def polygone(longueur_cote, nb_cotes, **params) :
    if "color" in params.keys() :
        turtle.color(params["color"])
    if "pensize" in params.keys():
        turtle.pensize(params["pensize"])
    for _ in range(nb_cotes):
        turtle.forward(longueur_cote)
        turtle.left(360 / nb_cotes)

def carre(longueur_cote, **params):
    polygone(longueur_cote, 4, **params)

def triangle(longueur_cote, **params):
    polygone(longueur_cote, 3, **params)

def maison(longueur_cote):
    carre(longueur_cote, color='green', pensize=2)
    turtle.right(90)
    turtle.back(longueur_cote)
    turtle.left(90)
    triangle(longueur_cote, color='blue', pensize=3)

maison(100)
turtle.done()