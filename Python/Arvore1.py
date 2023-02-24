
class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.dir = None
        self.esq = None

    def __repr__(self):
        return "%s -> %s <- %s" % (self.esq and self.esq.dado, self.dado, self.dir and self.dir.dado)

class Arvore:
    def __init__(self):
        self.raiz = None
    
    def inserir(self,dado):
        if self.raiz is None:
            novo_nodo = Nodo(dado)
            self.raiz = novo_nodo
        elif dado < self.raiz.dado:
            if self.raiz.esq is None:
                novo_nodo = Nodo(dado)
                self.raiz.esq = novo_nodo
            else:
                subarvore = Arvore()
                subarvore.raiz = self.raiz.esq
                subarvore.inserir(dado)
        else:
            if self.raiz.dir is None:
                novo_nodo = Nodo(dado)
                self.raiz.dir = novo_nodo
            else:
                subarvore = Arvore()
                subarvore.raiz == self.raiz.dir
                subarvore.inserir(dado)

    def busca(self,elemento): 
        if self.raiz is None:
            return False
        
        elif self.raiz.dado == elemento:
            return True
    
        elif elemento < self.raiz.dado:
            subarvore = Arvore()
            subarvore.raiz = self.raiz.esq
            return subarvore.busca(elemento)
        
        else:
            subarvore = Arvore()
            subarvore.raiz = self.raiz.dir
            return subarvore.busca(elemento)

    def __str__(self):
        if self.raiz is None:
            return False
        else:
            print

    def menor(self):
        menorDado = self.raiz.dado
        subE=Arvore()
        subE.raiz=self.raiz.esq
        if subE.raiz is not None:
            menorDado = subE.menor()
        return menorDado

    def maior(self):
        maiorDado = self.raiz.dado
        subD=Arvore()
        subD.raiz=self.raiz.dir
        if subD.raiz is not None:
            maiorDado = subD.maior()
        return maiorDado

























