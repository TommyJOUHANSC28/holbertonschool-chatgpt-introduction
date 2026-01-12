#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description :
        Calcule la factorielle d’un nombre entier n de manière récursive.

    Paramètres :
        n (int) : un entier positif ou nul dont on veut calculer la factorielle.

    Valeur de retour :
        int : la factorielle de n.
    """
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Récupération de l’argument donné en ligne de commande,
# conversion en entier, puis calcul de la factorielle
f = factorial(int(sys.argv[1]))

# Affichage du résultat
print(f)