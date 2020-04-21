#le joueur doit tapper un numéro compris entre 0 et 49 pour miser.
#choix de la console aléatoire d'un nombre compris entre 0 et 49 qui est soit noir ou rouge ( Introduction du module random )
#même numéro et couleur gagnant
#même couleur mais pas le même rend la moitier de sa mise
#rien des deux perd sa mise

#if et elif et else


#indiqué l'argent qu'il lui reste dans la bourse
#le joueur doit miser sur un nombre compris entre 0 et 49 et doit miser avec sa bourse.
#retirer la somme miser de la bourse
#randomiser la roulette pour obtenir un nombre aléatoire.
#Dire si le nombre du joueur et le même que sur la roulette c'est gagné et ajouté 3 fois la mise jouer a la bourse.
#Dire si le nombre est de la même parité que le nombre sur lequel le joueur à miser si c'est le cas le joueur gagne 50 % de la somme misé
#ajouter 50% de la mise jouer dans la bourse du joueur
#Si le joueur n'a aucun des deux le joueur perd sa mise
import os
from random import randrange
from math import ceil


bourse = 100
print ("Vous avez dans vôtre port monnaie",str(bourse),"€")


nb = int(input("Miser sur un nombre compris entre 0 et 49."))
while nb >= 0 and nb <= 49:
    print("Vous avez miser sur le nombre",str(nb))
    somme = int(input("Mise la somme que tu veux jouer"))
    print("Vous avez mis en jeux",str(somme),"€")
    break

mise_jouer = randrange(50)

try:
    print("le nombre de la roulette était",str(mise_jouer))
    if mise_jouer == nb:
        print("Vous avez gagner et remporter 3X vôtre mise")
        if mise_jouer % 2:
            print("Vous remportez la moitier de vôtre mise")
        else:
            print("Vous avez perdu vôtre mise")
    else:
         print("Vous avez perdu vôtre mise")
except NameError:
    print("vous n'avez pas choisis un bon nombre")



