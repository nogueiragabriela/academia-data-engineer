#Lista de exercícios sobre funções

#1
# def escreve_nome():
#     i = 0
#     while i < 5:
#         print("Academia Python")
#         i += 1

# escreve_nome()

#2
# def escreve_nome_com_retorno():
#     return "Academia Python"

# print(escreve_nome_com_retorno())

#3
# def verifica_sinal(numero):
#     if numero > 0:
#         return "p"
#     return "n"

# print(verifica_sinal(1))

#4
# def soma(n1, n2, n3):
#     return n1+n2+n3

# print(soma(1,2,3))

#5
def imprime_tabuada():
    for i in range(0, 11):
        multi = i * 9
        print("9 x {} = {}".format(i,multi))

imprime_tabuada()

#6
# def media(n1,n2,n3,n4):
#     media = (n1+n2+n3+n4)/4
#     if media <= 7 and media >= 5:
#         return "Está na média!"
#     elif media > 7:
#         return "Aprovada!"
#     return "Reprovado"

# print(media(7,7,7,7))

#7
# def soma_e_media(n1, n2, n3, n4,n5):
#     soma = n1 + n2 + n3 + n4 + n5
#     media = soma/5
#     return soma, media

# print(soma_e_media(1,2,3,4,5))

#8
# def media(*numeros):
#     soma = 0
#     j = 0
#     for i in numeros:
#         soma +=i
#         j+=1
#     media = soma/j
#     return soma, media

# print(media(1,2,3))

