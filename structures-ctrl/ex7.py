import turtle

cote = int( input('Coté du polygone : ') )
nb_cotes = int( input('Nb cotés : ') )
for _ in range(nb_cotes):
    turtle.forward( cote )
    turtle.left( 360/nb_cotes )
turtle.done()