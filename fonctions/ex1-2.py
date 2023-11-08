def puissance(nombre,exposant):
    """
    Renvoie la puissance du nombre
    :param nombre:
    :param exposant:
    :return:
    """

    return nombre ** exposant

def puissances(exposant, *nombres):
    for nombre in nombres:
        yield puissance(nombre, exposant)

print( list(puissances(2, 10, 11, 12)) )