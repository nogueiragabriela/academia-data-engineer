# Exercício: Receber 2 números inteiros via linha de comando
# e gerar os números inteiros que estão no intervalo entre eles

import sys

for i in range(int(sys.argv[1])+1, int(sys.argv[2])):
    print(i)

#No terminal: python3 ex19_intervalo.py numero1 numero2 

