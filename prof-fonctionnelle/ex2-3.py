import sqlite3

# Récup genres
cnx = sqlite3.connect('../_FICHIERS/streaming.sqlite')
curs = cnx.cursor()
curs.execute("Select * from genre")
genres = curs.fetchall()

genres = map( lambda film :  film[1].upper(), genres)
#genres = sorted(genres, key = lambda film : film[0] )
print(list(genres))
