class Horloge:

    def __init__(self,h=0,m=0,s=0) -> None:
        self.__heure = h
        self.__min = m
        self.__sec = s
        self.pub = 123

    def __str__(self) -> str:
        return f'{self.__heure}:{self.__min}:{self.__sec}'

    


h = Horloge(6,31,23)
print(h)
