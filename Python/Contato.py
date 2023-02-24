
class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone[3] = telefone
    
    def alterar_email(self, novo_email):
        self.email = novo_email
    
    def add_telefone(self, telefone):
        self.telefones.append(telefone)
    
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    
    def imprimir(self) -> None:
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"E-Mail: {self.email}")






























