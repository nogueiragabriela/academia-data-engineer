#Exercício: Um programa que peça via linha de comando o valor do tamanho do lado um quadrado 
# e faça o cálculo da área.

import sys

lado = float(sys.argv[1])

area = lado ** 2

print("A área do quadrado é igual a", area)

#No terminal: python3 .\areadoquadrado.py 3