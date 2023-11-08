nombres = range(1,1001)
impairs = list( filter( lambda nombre: nombre%2==1, nombres ) )
impairs = sorted(impairs, key=None, reverse=True)# key=None : pas de lambda de tri
print( list(impairs) )