#!/usr/bin/python3
# Correction de l'affichage des arguments
import sys
# Ajoute l'indice 1 pour commencer afficher l'argument
for i in range(1, len(sys.argv)):
    print(sys.argv[i])