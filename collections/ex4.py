couleurs_1 = {'rouge','vert','bleu'}
couleurs_2 = {'rouge','jaune'}
couleurs_1 = couleurs_2.union(couleurs_1) # union ne modifie pas l'objet ms renvoie le résultat
#couleurs_1.update( couleurs_2 )          # modifie l'objet mais ne renvoie rien
print( couleurs_1 )