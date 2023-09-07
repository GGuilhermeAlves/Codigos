from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
        
    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n Saldo insuficiente")
            
        elif valor >0:
            self._saldo -= valor
            print("\n Saque realizado com sucesso")
            return True
        
        else:
            print("\n Valor inválido")
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n Depósito realizado com sucesso")
        else:
            print("\n Valor inválido")
            return False
        
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        
    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes
            if transacao ["tipo"] == Saque.__name__]
        )
        
        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques >= self.limite_saques
        
        if excedeu_limite:
            print("\n O valor do saque excedeu o limite")
        elif excedeu_saque:
            print("\n O número de saques excedeu o limite")
        else:
            return super().sacar(valor)
        
        return False
    
    def __str__ (self):
        return f"""
            \n Agência: {self.agencia}
            \n C/C: {self.numero}	
            \n Titular: {self.cliente.nome}
        """
        
class Historico:
    def __init__(self):
        self._transacoes = []
        
    @property
    def transacoes (self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }  
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self, conta):
        pass
    
class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
        
    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
            
    @property
    def valor(self):
        return self._valor
        
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
            
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
                
def menu():
    menu = """\n
            em vindo ao Banco Python
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

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta")
        return 
        
    return cliente.contas[0]
    
def depositar(clientes):
    cpf = input ("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado")
        return
        
    valor = float(input("\n Informe o valor do depósito: "))
    transacao = Deposito(valor)
        
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
        
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado")
        return
    
    valor = float("Informe o valor do saque: ")
    transacao = Saque(valor)
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n Cliente não encontrado")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n Extrato")
    
def criar_cliente(clientes):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n Cliente já cadastrado")
        return
    
    nome = input("\n Informe o nome completo: ")
    data_nascimento = input("\n Informe a data de nascimento(dd-mm-aaaa): ")
    endereco = input("\n Informe o endereço(logradouro, numero - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome = nome, data_nascimento = data_nascimento, cpf = cpf, endereco = endereco)
    clientes.append(cliente)

    print("\n Cliente cadastrado com sucesso")
    
def criar_conta(numero_conta, clientes, contas):
    cpf = input("\n Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n Cliente não encontrado")
        return
    
    conta = ContaCorrente.nova_conta(cliente = cliente, numero = numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    
    print("\n Conta criada com sucesso")
    
def listar_contas(contas):
    for conta in contas:
        print (str(conta))

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            print("Encerrando...")
            break
        else:
            print("Opção inválida")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            