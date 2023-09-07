#Básico de Python - Sistema Bancário

menu = """
Bem vindo ao Banco Python
O que deseja fazer?

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            
        else:
            print("Valor inválido")

    elif opcao == "s":
        valor = float(input("Informe o valor a ser sacado: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente")
            
        elif excedeu_limite:
            print("Limite excedido")
            
        elif excedeu_saque:
            print("Limite de saques excedido")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
        
        else:
            print("Valor inválido")
            
    elif opcao == "e":
            
        print("\n============ Extrato ============")
        print("Não foram realizadas movimentações"if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida")






















