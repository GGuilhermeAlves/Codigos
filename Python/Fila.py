class Nodo:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo
        
    def __repr__(self):
        return "%s -> %s" % (self.dado, self.proximo)

class Fila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
    
    def __repr__(self):
        return "[" + str(self.cabeca) + "]"
    
    def vazia(self):
        if self.cabeca == None:
            return True
        else:
            return False
        
    def insere(self, novo_dado):
        #insere um elemento no final da fila
        #cria um novo nodo com o dado a ser armazenado
        novo_nodo = Nodo(novo_dado)
        #insere em uma fila vazia
        if self.vazia():
            self.cabeca = novo_nodo
            self.cauda = novo_nodo
        else:
        #faz com que o novo nodo seja o ultimo na fila
            self.cauda.proximo = novo_nodo
        #faz com que o último da fila referencie o novo nodo
            self.cauda = novo_nodo
    
    def pop(self):
        #remove o ultimo elemento da fila e o retorna
        #armazena o dado que está sendo removido
        #ajusta a cabeça
        #se ela passou a referenciar None a cauda segue junto
        #returna o valor removido
        removido = self.cabeca.dado()
        self.cabeca = self.cabeca.proximo
        if self.cabeca == None:
            self.cauda = None   
        return removido
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    