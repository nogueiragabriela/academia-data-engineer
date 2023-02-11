#Exercício: Um programa que peça um idade via input de usuário e exiba se a pessoa é maior ou menor de idade.

idade = int(input("Digite a idade: "))

if idade < 18:
    print("A pessoa é menor de idade.")
else:
    print("A pessoa é maior de idade.")