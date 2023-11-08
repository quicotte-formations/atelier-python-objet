import sqlite3

# Récup films
cnx = sqlite3.connect('../_FICHIERS/streaming.sqlite')
curs = cnx.cursor()
curs.execute(('SELECT * FROM film'))
films = curs.fetchall()

# Transfo dictionnaire pour ne pas jouer avec indice numériques ( pas pratiques )
films = map(lambda film: {'titre': film[1], 'annee': film[2],'duree': film[3]}, films)

# Filtre films contenant 'nuit'
films_filtres = filter(lambda film: film['titre'].lower().count('nuit') > 0, films)

# Trie par année de sortie
films_filtres = list(sorted(films_filtres, key=lambda film: film['annee']))

# PRINT
# print(films_filtrees)
print( films_filtres )