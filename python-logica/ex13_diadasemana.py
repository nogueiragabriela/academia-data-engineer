#Exercício 5: Leia um número via input de usuário e exiba ov dia correspondente da semana 
# (1- Domingo, 2- Segunda, ...). Para valores negativous ou maiores que 7 exibir "Valor inválido"

#Usando dicionario
numero = input("Digite um número: ")

lista = {"1": "Domingo", 
"2": "Segunda-feira", 
"3": "Terça-feira", 
"4": "Quarta-feira", 
"5": "Quinta-feira", 
"6": "Sexta-feira", 
"7": "Sabado"}

if numero in lista:
    print("O dia da semana é", lista[numero])
else:
    print("Valor inválido")

#Usando dicionario com numeros inteiros
# numero = int(input("Digite um número: "))

# lista = {1: "Domingo", 
# 2: "Segunda-feira", 
# 3: "Terça-feira", 
# 4: "Quarta-feira", 
# 5: "Quinta-feira", 
# 6: "Sexta-feira", 
# 7: "Sabado"}

# if numero in lista:
#     print(lista[numero])
# else:
#     print("Valor inválido")

#Direto por if
# numero = int(input("Digite um número: "))

# if numero == 1:
#     print("Domingo")
# elif numero == 2:
#     print("Segunda-feira")
# elif numero == 3:
#     print("Terça-feira")
# elif numero == 4:
#     print("Quarta-feira")
# elif numero == 5:
#     print("Quinta-feira")
# elif numero == 6:
#     print("Sexta-feira")
# elif numero == 7:
#     print("Sábado")
# else:
#     print("Valor inválido")