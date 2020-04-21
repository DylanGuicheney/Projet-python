                                                            #introduction du mot cle try et except :
annee = input()
try: # On essaye de convertir l'année en entier
    annee = int(annee2010)
except:
    print("Erreur lors de la conversion de l'année.")



try:
    resultat = numerateur / denominateur
except:
    print("Une erreur est survenue... laquelle ?")


try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")

                                                            # On peut créer autant de except que l'on veut.
                                                            # Introduction des types d'exceptions 

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")

                                                            # Introduction du mot cle (as)

#try:
#    # Bloc de test
#except type_de_l_exception as exception_retournee:
#    print("Voici l'erreur :", exception_retournee)

                                                            # Introduction du mot cle else

try:
    resultat = numerateur / denominateur
except NameError:
    print("La variable numerateur ou denominateur n'a pas été définie.")
except TypeError:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
except ZeroDivisionError:
    print("La variable denominateur est égale à 0.")
else:
    print("Le résultat obtenu est", resultat)

                                                            # Introduction du mot cle finally

#try:
    # Test d'instruction
#except type_de_l_exception:
    # Traitement en cas d'erreur
#finally:
    # Instruction(s) exécutée(s) qu'il y ait eu des erreurs ou non

                                                            # Introduction du mot cle pass

#try: 
    # try ne peut être seul.

#try:
    # Test d'instruction
#except type_de_l_exception: # Rien ne doit se passer en cas d'erreur
#    pass

                                                            # Introduction du mot cle assert 

var = 5
assert var == 5
#assert var == 8

annee = input("Saisissez une année supérieure à 0 :")
try:
    annee = int(annee) # Conversion de l'année
    assert annee > 0
except ValueError:
    print("Vous n'avez pas saisi un nombre.")
except AssertionError:
    print("L'année saisie est inférieure ou égale à 0.")
else:
    print("bien joué")

                                                            # Introduction comment lever une exception
                                                            # Introduction du mot cle raise

# raise TypeDeLException("bonjour")

annee = input() # l'utilisateur saisit l'année
try:
    annee = int(annee) # On teste de convertir l'année
    if annee<=0:
        raise ValueError("l'année saisie est négative ou nulle")
except ValueError:
    print("La valeur saisie est invalide (l'année est peut-être négative)")