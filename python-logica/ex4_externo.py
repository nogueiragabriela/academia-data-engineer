import sys

print("Argumentos que recebemos" + str(sys.argv))
print("Array de argumentos", sys.argv)
#Retorna um array dos argumentos que foram passados via linha de comando

print("Primeiro argumento: ", str(sys.argv[0]))
#Retorna o nome do arquivo, nesse caso seria .\externo.py

print("Segundo argumento: " + str(sys.argv[1]))
#Retorna o primeiro argumento passado via linha de comando

# Para passar as informações via linha de comando coloca-se no terminal: python3 .\externo.py arg1 arg2  

nome = sys.argv[3]
print(nome)

# Exercício: Usando informações via linha de comando, receba um valor numérico e exiba mensagem

print("Valor recebido:", sys.argv[1])
#No terminal: python3 externo.py arg1 arg2 
