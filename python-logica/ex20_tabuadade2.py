# Exercício: Usar um loop para exibir a tabuada de 2.
# num_tabuada = 2
# tabuada = 0

# while tabuada <= 10:
#   print(f'{num_tabuada} x {tabuada} = {num_tabuada * tabuada}')
#   tabuada +=1

lista = [0,1,2,3,4,5,6,7,8,9,10]
for i in lista:
    multi = i * 2
    print("2 x {} = {}".format(i,multi))