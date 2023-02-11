# Exercício: Um programa que leia 5 números via input de 
# usuário e exiba qual é o maior número, usando estruturas de repetição

maior = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero

print(f"O maior número é {maior}")
        
            

        
        

