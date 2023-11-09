import turtle

class Horloge:

    def __init__(self,h,m,s) -> None:
        """
        Initialise avec validation
        :param h:
        :param m:
        :param s:
        """
        if h<0 or h>11:
            self.heure = 0
        else:
            self.heure = h
            
        if m<0 or m>59:
            self.min = 0
        else:
            self.min = m
            
        if s<0 or s>59:
            self.sec = 0
        else:
            self.sec = s

    def __str__(self) -> str:
        return f'{str(self.heure).zfill(2)}:{str(self.min).zfill(2)}:{str(self.sec).zfill(2)}'

    def avance_une_seconde(self):
        self.sec += 1
        if self.sec > 59:
            self.sec=0
            self.min += 1
        if self.min > 59:
            self.min = 0
            self.heure += 1
        if self.heure>11:
            self.heure = 0

    def affiche_aiguille(pos, max, couleur, pensize, longueur):

        # Calcule angle
        angle = 360 / max * pos

        # Dessine aiguille
        turtle.up()
        turtle.home()
        turtle.down()
        turtle.color(couleur)
        turtle.pensize(pensize)
        turtle.left(90)
        turtle.right(angle)
        turtle.forward(longueur)


    def affiche_avec_turtle(self):


        # Dessine cadran
        RAYON = 250

        turtle.up()
        turtle.home()
        turtle.right(90)
        turtle.forward(250)
        turtle.left(90)
        turtle.down()
        turtle.color('black')
        turtle.circle(RAYON)

        # Dessine aiguilles
        Horloge.affiche_aiguille(self.heure,12,'red',10,100)
        Horloge.affiche_aiguille(self.min, 60, 'blue', 5, 200)
        Horloge.affiche_aiguille(self.sec, 60, 'green', 2, 200)


turtle.speed(0)
horloges = [ Horloge(11,59,59), Horloge(10,59,59), Horloge(10,30,59), Horloge(10,5,5) ]
for horloge_actuelle in horloges:
    print( horloge_actuelle )
    horloge_actuelle.avance_une_seconde()
    print( '+ une sec -> ', horloge_actuelle )
    horloge_actuelle.affiche_avec_turtle()
    input('Appuyez pour la suite')
    turtle.clear()
