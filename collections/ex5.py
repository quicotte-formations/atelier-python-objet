entiers_1 = [1,2,3,4,5]
entiers_2 = [2,3,4]
#entiers_1 = [ nombre_actuel for nombre_actuel in entiers_1 if nombre_actuel not in entiers_2 ] # liste avec compréhension
entiers_1 = set(entiers_1) - set(entiers_2)
print( entiers_1 )

