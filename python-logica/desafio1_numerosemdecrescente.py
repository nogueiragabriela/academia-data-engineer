# Desafio: Ler via linha de comando 3 números e mostrar em ordem decrescente.

import sys

numeros = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
ordem = sorted(numeros, reverse = True)

print(ordem)

#No terminal: python3 .\numerosemdecrescente.py 56 1 200