#!/usr/bin/python3
# Calcul de la factorielle corrigé
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
# Décrementation de n à chaque tour
        n -= 1
    return result

f = factorial(int(sys.argv[1]))
print(f)