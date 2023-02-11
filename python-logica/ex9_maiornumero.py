#Exercício: Um programa que peça 2 números via linha de comando e imprima o maior deles.

import sys

numero1 = float(sys.argv[1])
numero2 = float(sys.argv[2])

if numero1 > numero2:
    print(numero1)
else:
    print(numero2)

#No terminal: python3 .\maiornumero.py 14 20

