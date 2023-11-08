def nb_premier(nombre):
    if nombre==1:
        return False
    for i in range(2,nombre):
        if nombre%i==0:
            return False
    return True

nombres = range(1,1001)
impairs = filter( lambda nombre: nombre%2==1, nombres )

nombres_premiers = list(filter( nb_premier, impairs ))# Version courte : on passe en 1er arg le nom de la fonction
#nombres_premiers = list(filter( lambda nombre: nb_premier(nombre), impairs ))# Version longue avec lambda qui délègue à nb_premier
print(nombres_premiers)