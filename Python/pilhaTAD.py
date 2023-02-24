class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada."""
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s <- %s' % (self.anterior, self.dado)

class Pilha:
    """Esta classe representa uma pilha usando uma estrutura encadeada."""
    tamanho=0
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"
    
    def vazia(self):
        """Retorna True se a pilha está vazia e False caso contrário."""
        if(self.topo==None):
            return True
        else:
            return False
        
    def insere(self, novo_dado):
        """Insere um elemento no final da pilha."""
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
    
        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo
        
        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo
        __class__.tamanho+=1
        
    def remove(self):
        """Remove o elemento que está no topo da pilha."""
        
        if(self.vazia()):
            print("Impossível remover valor de pilha vazia.")
        else:
            __class__.tamanho-=1
            removido=self.topo.dado
            self.topo = self.topo.anterior
            return removido

