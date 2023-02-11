# Exercício: Um programa que exiba a tabuada de 2 até a de 9, usando loops.

lista1 = [2,3,4,5,6,7,8,9]
lista2 = [0,1,2,3,4,5,6,7,8,9,10]
for i in lista1:
    for j in lista2:
        multi = i * j
        print("{} x {} = {}".format(i,j,multi))