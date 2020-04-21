import os 

def test():
    annee = 2000
    if (annee % 4 == 0) and ((annee % 100 != 0) or (annee % 400 == 0)):
        print("l'année est bi")
    else:
        print("l'année n'est pas bi")

def test2():
    print('test 2') 