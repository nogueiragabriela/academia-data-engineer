#Exercício: Um programa que leia 3 números via linha de comando e imprima o maior deles.

import sys

numero1 = float(sys.argv[1])
numero2 = float(sys.argv[2])
numero3 = float(sys.argv[3])

if numero1 > numero2 and numero1 > numero3:
    print(numero1)
elif numero2 > numero1 and numero2 > numero3:
    print(numero2)
else:
    print(numero3)


#No terminal: python3 .\maiornumerode3.py 14 20 65