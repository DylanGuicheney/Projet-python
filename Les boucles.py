                                                                        #while = tant que (boucle)
                                                                        #def = Début d'appelle d'une fonction 


                                                                        #introduction du mot clef def
def table_de_7(nb):
    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < 10: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb, "=", (i + 1) * nb)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.
table_de_7(7)

def table(nb2, max):
    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < max: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nb2, "=", (i + 1) * nb2)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.
table(11, 20)#

def table3(nb3, max=10):
    """Fonction affichant la table de mulyiplication par nb3 de 1*nb3 à max*nb3
    (max >=0) """
    i = 0
    while i < max:
        print(i + 1,"*", nb3, "=", (i + 1) * nb3)
        i += 1
table3(40)


                                                                                # introduction du mot clef return
def carre(valeur):
    return valeur * valeur

variable = carre(5)

                                                            #Découverte du mot lambda mais l'utilisation n'est pas encore dans mon cours
f = lambda x: x * x 
f(5)


                                                            #Découverte des modules (La méthode) et du mot clef import

import math
math.sqrt(16)
print(math.sqrt(16))

                                                            #espace de noms spécifique

import math as mathematiques
mathematiques.sqrt(25)
print(mathematiques.sqrt(25))

                                                            #Autre méthode d'importation from ..... Import .....

from math import fabs
fabs(-5)
print(fabs(2))

