import sqlite3

cnx = sqlite3.connect('_FICHIERS/streaming.sqlite')
curs = cnx.cursor()
curs.execute('SELECT * FROM film')
films  = curs.fetchall()

# Filtre films de 2014
films = filter( lambda film: film[2]==2014, films )
films = list( filter( lambda film: film[3]!=None and film[3]>90 and film[3]<120, films ) )

# Transfo
films = list( map( lambda film: {'titre': film[1], 'annee': film[2], 'duree': film[3]}, films) )

# Tri
films = list( sorted( films, key=lambda film: film['duree'] ) )
None