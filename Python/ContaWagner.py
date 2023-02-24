
from datetime import date
from abc import ABC, abstractmethod

class SaldoExcecaoError(Exception):
    def __str__(self):
        return "Saldo insuficiente"

class Autenticavel(ABC):
    @abstractmethod
    def autenticar(self= bool,senha=str):
        pass

class Conta():
    def __init__(self, agencia=str, numConta=int, saldo=int, senha=str):
        self.agencia = agencia
        self.numConta = numConta
        self.saldo = saldo
        self.senha = senha

    def depositar(self, valor=float):
        try:
            senha = input("Digite a senha: ")
            if self.autenticar(senha):
                valor = float(input(f"Digite o valor a ser depositado:"))
                if valor < 0:
                    raise ValueError
                self.saldo += valor
            else:
                return "Senha incorreta"

        except ValueError:
            print("Valor inválido ou tipo inválido")
            
    def sacar(self):
        try:
            senha = input("Digite a senha: ")
            if self.autenticar(senha):
                valor = float(input(f"Digite o valor a ser sacado: ")) 
                if valor < 0:
                    raise ValueError  
                if valor > self.saldo:
                    raise SaldoExcecaoError
                else:
                    self.saldo -= valor
            else:
                return "senha incorreta"

        except SaldoExcecaoError as e:
            print(e)
        except ValueError:
            print("Valor ou tipo inválido")


    def autenticar(self= bool,senha=str):
        if self.senha == senha:
            return True
        else:
            return False

    def verSaldo(self):
        print(f"Saldo: {self.saldo}")   


class ContaPoupança(Conta):
    def __init__(self, agencia=str, numConta=int, saldo=float, senha=str, percRendimento=float):
        super().__init__(agencia, numConta, saldo, senha)
        self.percRendimento = percRendimento

    def calcularRendimento(self):
        self.saldo += (self.saldo * self.percRendimento / 100)

class ContaEspecial(Conta):
    def __init__(self, agencia=str, numConta=int, saldo=float, senha=str, limite=float, juros=float):
        super().__init__(agencia, numConta, saldo, senha)
        self.limite = limite
        self.juros = juros

    def debitarJuros(self):
        if date.today().day == 1:
            self.saldo -= (self.saldo * self.juros / 100)
