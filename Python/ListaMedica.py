#Bruno Mendes
#Wagner Guilherme
#João Victor Tabosa

class Nodo:
    def __init__(self, dado, cor, proximo_dado=None):
        self.dado = dado
        self.proximo = proximo_dado
        self.cor = cor
        
    def __repr__(self) -> str:
        return '%s (%s) -> %s' %(self.dado, self.cor, self.proximo)
    
class Lista:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0
        
    def __repr__(self):
        return '[ ' + str(self.cabeca) + ' ]'

    def vazia(self):
        if self.cabeca == None:
            return True
        else:
            return False

    def inserir(self, novo_dado, cor='v'):
            if(cor != 'v' and cor != 'a'):
                cor = 'v'
            novo_nodo = Nodo(novo_dado, cor)
            if self.vazia():
                self.cabeca = novo_nodo
                self.cauda = novo_nodo
                self.tamanho += 1
            else:
                if(cor == 'a'):
                    self.inserir_prioridade(novo_dado)
                else:
                    self.inserir_fim(novo_dado)
                
    def inserir_fim(self, novo_dado):
        novo_nodo = Nodo(novo_dado, 'v')
        self.cauda.proximo = novo_nodo
        self.cauda = novo_nodo
        self.tamanho += 1

    def inserir_prioridade(self, novo_dado):
        novo_nodo = Nodo(novo_dado, 'a')
        aux = self.cabeca
        if self.cabeca == None:
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        elif self.cabeca.cor == 'v':
            novo_nodo.proximo = self.cabeca
            self.cabeca = novo_nodo
        else:
            while aux.cor == 'a':
                aux_a = aux
                aux = aux.proximo
                if aux == None:
                    self.cauda = novo_nodo
                    break
            novo_nodo.proximo = aux_a.proximo
            aux_a.proximo = novo_nodo
        self.tamanho += 1