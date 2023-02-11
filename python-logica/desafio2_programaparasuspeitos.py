"""
Desafio: Faça um programa que faça 5 perguntas para uma pessoa 
sobre um crime:
"Falou com a vítima no dia do crime?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia dinheiro para a vítima?"
"Já trabalhou com a vítima?"
Se a pessoa responder positivamente a 2 questões ela deve ser 
considerada como "Suspeita, 
entre 3 e 4 como "Cúmplice" e 5 como "Assassina".
Caso contrário será classificada como "Inocente".
"""
print("Responda as perguntas abaixo usando S para Sim e N para Não:")

resposta1 = input("Falou com a vítima no dia do crime (S/N)?").upper()
resposta2 = input("Esteve no local do crime (S/N)?").upper()
resposta3 = input("Mora perto da vítima (S/N)?").upper()
resposta4 = input("Devia dinheiro para a vítima (S/N)?").upper()
resposta5 = input("Já trabalhou com a vítima (S/N)?").upper()

respostas = [resposta1, resposta2, resposta3, resposta4, resposta5]

if respostas.count("S") == 2:
    print("Pessoa classificada como Suspeita")
elif respostas.count("S") == 3 or respostas.count("S") == 4:
    print("Pessoa classificada como Cúmplice")
elif respostas.count("S") == 5:
    print("Pessoa classificada como Assassina")
else:
    print("Pessoa classificada como Inocente")




        

