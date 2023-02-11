#Exercício: Receber 2 notas de uma aluna via input de usuário, calcular a média e apresentar a situação final.
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2


if media >= 7 and media < 10: 
    print("Aprovado.")
elif media == 10:
    print("Aprovado com distinção.")
else:
    print("Reprovado.")
