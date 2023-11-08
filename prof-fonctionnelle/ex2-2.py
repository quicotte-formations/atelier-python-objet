import sqlite3

# Récup films
cnx = sqlite3.connect('../_FICHIERS/streaming.sqlite')
curs = cnx.cursor()
curs.execute(('SELECT * FROM film'))
films = curs.fetchall()

# Filtre films de vampires
films3 = filter(lambda film: film[1].lower().count('vampire') > 0, films)
# films3=list(filter(lambda film: 'vampire' in film[1].lower(), films))# IDEM avec opérateur in

# Filtre par durée > 90
films4 = filter(lambda film: film[3] > 90, films3)

# Tri par titre
films5 = sorted(films4, key=lambda film: film[1])

print(list(films5))