caixinhas = {}

def caixinha():
    while True:
        atividade = input("Atividade: ")

        if atividade == "adicionar":
            nome_da_caixinha = validar_nome()
            valor = validar_valor()
            adicionar(nome_da_caixinha, valor)  
        elif atividade == "retirar":
            nome_da_caixinha = validar_nome()
            valor = validar_valor()
            retirar(nome_da_caixinha, valor)
        elif atividade == "saldo":
            nome_da_caixinha = validar_nome()
            saldo(nome_da_caixinha)
        elif atividade == "sair":
            sair()
            break
        else:
            print("Opção inválida! Por favor digite uma atividade (adicionar|retirar|saldo|sair)")
            caixinha()

def validar_valor():
    numero_validado = False
    while not numero_validado:
        try:
            valor = float(input("Valor: "))
            if valor > 0:
                print("O valor digitado foi adicionado na caixinha com sucesso.")
                numero_validado = True
            else:
                print("Valor negativo! Por favor digite um valor válido positivo.")
        except ValueError:
            print("Valor inválido! Por favor digite um valor válido positivo.")

    return float(valor)

def validar_nome():
    nome_da_caixinha = input("Caixinha: ")
    while nome_da_caixinha.isspace() == True or nome_da_caixinha == "":
        print("Valor invalido")
        nome_da_caixinha = input("Caixinha: ")
    return nome_da_caixinha

def adicionar(nome_da_caixinha, valor):
    if nome_da_caixinha in caixinhas:
        caixinhas.get(nome_da_caixinha).append(valor)
    else:
        caixinhas[nome_da_caixinha] = [valor]

def retirar(nome_da_caixinha, valor):
    if nome_da_caixinha in caixinhas:
        caixinhas.get(nome_da_caixinha).append(-valor)
    else:
        caixinhas[nome_da_caixinha] = [-valor]
    
def saldo(nome_da_caixinha):
    if nome_da_caixinha not in caixinhas:
        print(f"A caixinha {nome_da_caixinha} não existe no sistema.")
    else:
        print(f"Saldo da caixinha {nome_da_caixinha}:")
        for valor in caixinhas[nome_da_caixinha]:
            print("R$ {:,.2f}".format(valor))
    
def sair():
    print("Saindo do programa.")

caixinha()