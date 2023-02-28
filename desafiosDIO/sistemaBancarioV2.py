
def menu():
    menu = """\n
            Bem vindo ao Banco Python
                O que deseja fazer?
                
    [d]\tDepósito
    [s]\tSaque
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNova Usuário
    [q]\tSair
    => """
    return input(menu).lower()

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f} \n"
        print("\n Depósito realizado com sucesso!")
    else:
        print("\n Valor inválido")
        
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saque
    
    if excedeu_saldo:
        print("\n Saldo insuficiente")
    elif excedeu_limite:
        print("\n Limite excedido")
    elif excedeu_saque:
        print("\n Limite de saques excedido")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saque += 1
        print("\n Saque realizado com sucesso!")
    else:
        print("Valor inválido")
    
    return saldo, extrato

def extrato(extrato, saldo):
    print("\n============ Extrato ============")
    print("Não foram realizadas movimentações"if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===================================")
    
def novo_usuario(usuario):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario:
        print("\n CPF já cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço(logradouro, numero - bairro - cidade/sigla estado): ")
    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n Usuario criado com sucesso!")
        
        
def filtrar_usuario(cpf, usuario):
    for u in usuario:
        if u["cpf"] == cpf:
            return u
    return None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF: ")
    usuario = filtrar_usuario(cpf, usuario)
    
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuario não encontrado")
    
def listar_contas(contas):
    print("\n============ Contas ============")
    for conta in contas:
        print(f"Agência: {conta['agencia']}")
        print(f"Conta: {conta['numero_conta']}")
        print(f"Nome: {conta['usuario']['nome']}")
        print(f"CPF: {conta['usuario']['cpf']}")
        print("===================================")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            valor = float(input("Informe o valor a ser depositado: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Informe o valor a ser sacado: "))
            
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                numaro_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )
    
        elif opcao == "e":
            extrato(saldo, extrato = extrato)
        
        elif opcao == "nu":
            novo_usuario(usuarios)
            
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif opcao == "lc":
            listar_contas(contas)
            
        elif opcao == "q":
            break
