#== égal
#!= différent
#>= supérieur ou égal
#<= inférieur ou égal

# On fait un test pour savoir si a est comprise dans l'intervalle allant de 2 à 8 
# a = 8
# if a >= 2 not a>8:
#     print("a est dans l'intervalle.")
# else:
#     print("a n'est pas dans l'intervalle.")

# majeur = False
# if majeur is not True:
#     print("Vous n'êtes pas encore majeur.")

#Vous n'êtes pas encore majeur.

#pas un multiple de 100
#multiple de 400

annee = int(input("Saisir une année : "))
if (annee % 4) == 0:
    if (annee % 100) == 0:
        if (annee % 400) == 0:
            print("l'année est bi")
        else:
            print("l'année n'est pas bi")
    else:
        print("l'année est bi")
else:
    print("l'année n'est pas bi")

#essai de réaliser la même opération mais en plus court. Sans utilisation répétter du IF.

if (annee % 4 == 0) and ((annee % 100 != 0) or (annee % 400 == 0)):
    print("l'année est bi")
else:
    print("l'année n'est pas bi")


