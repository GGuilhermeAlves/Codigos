### de: Wagner Guilherme Alves da Silva

class Pagavel:
    def get_valor_a_pagar(self):
        pass

class Empregado(Pagavel):
    def __init__(self, nome, sobrenome, numero_identificacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.numero_identificacao = numero_identificacao

    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_numero_identificacao(self):
        return self.numero_identificacao

    def __str__(self):
        return f"{self.get_nome()} {self.get_sobrenome()}\nNumero de identificação: {self.get_numero_identificacao()}"

class Comissionado(Empregado):
    def __init__(self, nome, sobrenome, numero_identificacao, vendas):
        super().__init__(nome, sobrenome, numero_identificacao)
        self.vendas = vendas

    def ganhos_vendas(self):
        return self.get_vendas() * 0.6

    def get_valor_a_pagar(self):
        return self.ganhos_vendas()

    def get_vendas(self):
        return self.vendas

    def set_vendas(self, vendas):
        self.vendas = vendas

    def __str__(self):
        return f"{'Comissionado'}: {super().__str__()}\n{'Valor vendas'}: ${self.get_vendas():,.2f}; {'Valor comissão'}, {self.ganhos_vendas():,.2f}"

class AssalariadoComissionado(Comissionado):
    def __init__(self, nome, sobrenome, numero_identificacao, vendas):
        super().__init__(nome, sobrenome, numero_identificacao, vendas)
        self.salario = 954

    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        self.salario = salario

    def get_valor_a_pagar(self):
        return super().ganhos_vendas() + self.get_salario()

    def __str__(self):
        return f"{'assalariado'} {super().__str__()}\n{'Salario total'}: ${super().ganhos_vendas() + self.get_salario():,.2f}"

