def mots_en_majuscules(mots:list):
    for i, mot in enumerate(mots):
        yield mot
        mots[i] = mot.upper()

les_mots = ['hello','coucou']
print( list(mots_en_majuscules(les_mots)) )
print( les_mots )