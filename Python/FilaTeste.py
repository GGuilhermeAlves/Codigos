class Nodo:
    def __init__(self, dado, cor='v', proximo_dado=None):
        self.dado = dado
        self.proximo = proximo_dado
        self.cor = cor
        
    def __repr__(self) -> str:
        return '%s (%s) -> %s' %(self.dado, self.cor, self.proximo)
    
class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        
    def __repr__(self):
        return '[' + str(self.cabeca) + ']'

    def vazia(self):
        if self.cabeca == None:
            return True
        else:
            return False
    
    def inserir(self, novo_dado, cor='v'):
        novo_nodo = Nodo(novo_dado, cor)
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
            self.tamanho += 1
        else:
            self.cauda.proximo = novo_nodo
            self.cauda = novo_nodo
            self.tamanho += 1

    def remove(self):
        removido = self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        if self.cabeca == None:
            self.cauda == None
        self.tamanho -= 1
        return removido

    def inserirPrioridade(self, novo_dado, cor='a'):
        novo_nodo = Nodo(novo_dado, cor)
        if self.cabeca == None:
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        elif self.cabeca.cor == 'v':
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        else:
            aux = self.cabeca
            while aux.cor == 'a':
                aux_a = aux
                aux = aux.proximo
                if aux == None:
                    self.cauda = novo_nodo
                    break
            novo_nodo.proximo = aux_a.proximo
            aux_a.proximo = novo_nodo
        self.tamanho += 1

fila1 = Fila()
print(fila1)
fila1.inserir(21)
fila1.inserir(22)
fila1.inserir(23)
print(fila1)
fila1.inserirPrioridade(2)
print(fila1)
fila1.inserirPrioridade(1)
print(fila1)
fila1.inserir(23)
print(fila1)
fila1.remove()
print(fila1)
fila1.inserirPrioridade(4)
fila1.inserirPrioridade(3)
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.inserir(24)
print(fila1)
print(fila1.tamanho)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.inserirPrioridade(1)
print(fila1)
fila1.inserirPrioridade(2)
print(fila1)
fila1.inserirPrioridade(3)
print(fila1)
fila1.inserir(4)
print(fila1)
fila1.inserirPrioridade(5)
print(fila1)
fila1.inserir(6)
print(fila1)
print(fila1.tamanho)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.inserirPrioridade(30)
fila1.inserirPrioridade(31)
fila1.inserirPrioridade(32)
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.inserirPrioridade(33)
fila1.inserirPrioridade(34)
print(fila1)
print(fila1.tamanho)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
fila1.remove()
print(fila1)
print(fila1.tamanho)
