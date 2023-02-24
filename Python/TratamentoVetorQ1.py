## Tratamento de exceções em vetores Questão 1
## por: Wagner Guilherme Alves da Silva

vetor = []
i = 0
while True:
    try:
        valor = int(input(f"Digite o {i+1}° valor inteiro e digite 0 para encerrar: "))
        if len(vetor) == 10:
            raise IndexError
        if valor == 0:
            print("Encerrando...")
            break
        vetor.append(valor)
        i += 1
    except ValueError:
        print("Tipo inválido")
    except IndexError:
        print("Tamanho do vetor previsto foi excedido.")
        break
print(f"Valores do vetor: {vetor}")
    
    
