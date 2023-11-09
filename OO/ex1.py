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
            self.__heure = 0
        else:
            self.__heure = h
            
        if m<0 or m>59:
            self.__min = 0
        else:
            self.__min = m
            
        if s<0 or s>59:
            self.__sec = 0
        else:
            self.__sec = s

    def __str__(self) -> str:
        return f'{str(self.__heure).zfill(2)}:{str(self.__min).zfill(2)}:{str(self.__sec).zfill(2)}'

    def avance_une_seconde(self):
        self.__sec += 1
        if self.__sec > 59:
            self.__sec=0
            self.__min += 1
        if self.__min > 59:
            self.__min = 0
            self.__heure += 1
        if self.__heure>11:
            self.__heure = 0

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
        Horloge.affiche_aiguille(self.__heure, 12, 'red', 10, 100)
        Horloge.affiche_aiguille(self.__min, 60, 'blue', 5, 200)
        Horloge.affiche_aiguille(self.__sec, 60, 'green', 2, 200)


turtle.speed(0)
horloges = [ Horloge(11,59,59), Horloge(10,59,59), Horloge(10,30,59), Horloge(10,5,5) ]
for horloge_actuelle in horloges:
    print( horloge_actuelle )
    horloge_actuelle.avance_une_seconde()
    print( '+ une sec -> ', horloge_actuelle )
    horloge_actuelle.affiche_avec_turtle()
    input('Appuyez pour la suite')
    turtle.clear()
