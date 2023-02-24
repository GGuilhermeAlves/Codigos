class Nodo:
    """Esta classe representa um nodo de uma estrutura encadeada."""
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class Fila:
    """Esta classe representa uma fila usando uma estrutura encadeada."""
    def __init__(self):
        self.cabeca = None
        self.cauda   = None
        self.tamanho=0

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def vazia(self):
        if(self.cabeca != None):
            return False
        else:
            return True
    
    def insere(self, novo_dado):
        """Insere um elemento no final da fila."""
        self.tamanho+=1
        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)
        # Insere em uma fila vazia.
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
            # Faz com que o novo nodo seja o último da fila.
            self.cauda.proximo = novo_nodo
            # Faz com que o último da fila referencie o novo nodo.
            self.cauda =novo_nodo 
            
    def remove(self):
        """Remove o último elemento da fila."""
        self.tamanho-=1
        removido=self.cabeca.dado
        self.cabeca = self.cabeca.proximo
        if self.cabeca == None:
            self.cauda = None
        return removido
        
    