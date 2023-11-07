entiers = range(2, 11, 2)

# Itératif
print( 'SOL ITERATIVE :' )
print('------------------------------')
for element in entiers:
   print( element )

# Comprehension list v A
print( 'SOL COMPREHENSION LIST V A:' )
print('------------------------------')
print([entier for entier in entiers])

# Comprehension list v B
print( 'SOL COMPREHENSION LIST V B:' )
print('------------------------------')
[print(entier) for entier in entiers]