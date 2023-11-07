import random

alea = random.randint(1,100)
guess = -1
while guess != alea :
    try:
        guess = int( input("Entrez un nombre entre 1 et 100:") )
    except:
        print('Nombre invalide !')
        continue
    if guess > alea :
        print('Le nombre recherché est plus petit')
    elif guess < alea :
        print("Le nombre recherché est plus grand")
print("BRAVO!")