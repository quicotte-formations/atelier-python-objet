import turtle

cote = int( input('Coté du carré : ') )
turtle.clear()
for _ in range(4):
    turtle.forward(cote)
    turtle.left(90)
turtle.done()