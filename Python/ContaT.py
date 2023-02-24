from datetime import date
class Conta:
    def __init__(self, nome, conta, saldo=100):
        self._nome_cliente = nome
        self._num_conta = conta
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome_cliente

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo = saldo

    def sacar(self, valor):
        if (self.saldo < valor):
            pass
        else:
            self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor

    def imprimir(self):
        print(f'Titular: {self.nome}\nSaldo: {self.saldo}')


class ContaPoupanca(Conta):
    def __init__(self, nome, conta, saldo, dia):
        super().__init__(nome, conta, saldo )
        self.dia_rendimento = dia
        self.hoje = date.today().day

    def calcularNovoSaldo(self, taxa):
        if (self.hoje >= self.dia_rendimento):
            self.saldo += (self.saldo * taxa / 100)

class ContaEspecial(Conta):
    def __init__(self, nome, conta, saldo, limite):
        super().__init__(nome, conta, saldo)
        self._limite = limite
        self.limiteInicial = limite

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite
        
    def sacar(self, valor):
        if (self.saldo >= 0):
            if (valor > self.saldo):
                aux = (valor - self.saldo)
                if (aux <= self.limite):
                    self.saldo -= valor
                    self.limite -= aux
            else:
                self.saldo -= valor
        else:
            if (valor <= self.limite):
                self.limite -= valor
                self.saldo -= valor

    def depositar(self, valor):
        self.saldo += valor
        if (self.saldo >= 0):
            self.limite = self.limiteInicial
        

    def imprimir(self):
        print(f'limite: {self.limite}')
        return super().imprimir()

conta1 = Conta('Joao', '123-4')
conta1.imprimir()
print('saquei 35')
conta1.sacar(35.0)
conta1.imprimir()
print('depositei 50')
conta1.depositar(50.0)
conta1.imprimir()
print('tentei sacar 250')
print(conta1.sacar(250.0))
conta1.imprimir()
print()
print()
conta2 = ContaEspecial('a', '11', 100.0, 50.0)
conta2.imprimir()
print()
print('saquei 30')
conta2.sacar(30.0)
print()
conta2.imprimir()
print()
print('tentei sacar 100')
conta2.sacar(100.0)
print()
conta2.imprimir()
print()
print('sanque de 20')
conta2.sacar(20.0)
print()
conta2.imprimir()
print()
print('depositei 250')
conta2.depositar(250.0)
conta2.imprimir()
print('depositei mais 250')
conta2.depositar(250.0)
conta2.imprimir()
print()
print('saque de 10')
conta2.sacar(10.0)
print()
conta2.imprimir()
print()
print()
conta3 = ContaPoupanca('Jose','123-5',100.0, 1)
conta3.imprimir()
print()
conta3.calcularNovoSaldo(10)
conta3.imprimir()
conta3.sacar(15.0)
conta3.imprimir()
print()
conta3.depositar(500.0)
conta3.imprimir()
