#Exercício: Um programa que peca 4 notas bimestrais via linha de comando e imprima a média.

import sys

media = (float(sys.argv[1]) + float(sys.argv[2]) + float(sys.argv[3]) + float(sys.argv[4]))/4

print("A média das notas é igual a", media)

#No terminal: python3 .\medianotas.py 7 8 9 10