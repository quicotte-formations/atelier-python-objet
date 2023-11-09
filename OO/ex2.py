class Vehicule:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def avancer(self):
        None

    def __str__(self):
        return f"Véhicule={self.__class__.__name__} X={self._x} Y={self._y}"

class Voiture(Vehicule):
    def avancer(self):
        self._x += 5

class Avion(Vehicule):
    def avancer(self):
        self._x += 100
        self._y += 10

class Twingo(Voiture):
    pass

class Ferrari(Voiture):
    def avancer(self):
        self._x += 50

class Boeing(Avion):
    def avancer(self):
        super().avancer()
        self._y += 5

class Mirage(Avion):
    def avancer(self):
        super().avancer()
        super().avancer()

vehicules = [Twingo(0,0), Ferrari(0,0), Boeing(0,0), Mirage(0,0)]
for vehicule in vehicules:
    print('Position initiale de ' + vehicule.__str__())
    vehicule.avancer()
    print(f'Position finale est : ' + vehicule.__str__())