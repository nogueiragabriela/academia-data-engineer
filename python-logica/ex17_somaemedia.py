# Exercício: Um programa que leia 5 números via input e exiba
# a soma e a média

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))
numero4 = int(input("Digite o quarto número:"))
numero5 = int(input("Digite o quinto número:"))

lista = [numero1, numero2, numero3, numero4, numero5]

soma = 0
print(lista)
for i in lista:
    soma = soma + i
    print(soma)

media = soma/5

print(f"A soma é igual a {soma} e a média é igual a {media}.")