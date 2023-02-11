#Exercício 6: Programa que leia via input de usuário um número correspondente a um determinado ano 
# e informe se esse ano é bissexto ou não.

ano = int(input("Digite um ano: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print("O ano é bissexto!")
else:
  print("O ano não é bissexto!")

"""
Explicação para a fórmula de verificação de ano bissexto: 
Faça um programa que pergunta um ano para a usuária e responde se ele é bissexto ou não.
A regra geral para determinar se um ano é bissexto é: todo ano divisível por 4, 
a princípio, é bissexto: 2016, 2020, 2024...
Porém existe uma exceção: anos divisíveis por 100 não são bissextos. 
O ano 2100, por exemplo, é divisível por 4, mas como também é divisível por 100, ele não pode ser bissexto.
A exceção possui uma exceção: anos divisíveis por 400 são bissextos. 
O ano 2000, por exemplo, é divisível por 100. Porém, como ele também é divisível por 400, ele torna-se bissexto.
"""