import random
import os
lista = []
i=0
cont=3
aleatorio=random.randint(0,10)

while True:
    print(f"Programa de adivinhação, você tem {cont} tentativas!")
    entra = (input("Digite um número de 0 a 10: "))
    print (aleatorio)
    if entra.isnumeric() == False and int(entra) >= 10 and int(entra) < 0 :
        print("Opção inválida")
    else: 
        entra = int(entra)
        if entra == aleatorio:
            os.system("cls")
            print("Você acertou!")
            cont = 1
        elif entra > aleatorio:
            print(f"Você errou! Tente novamente Dica: O número {entra} está maior")
        else:
            print(f"Você errou! Tente novamente Dica: O número {entra} está menor")
        cont -= 1
        if cont == 0:
            print("Deseja jogar novamente?")
            recomecar = str(input("Digite 'S'(Sim) para jogar novamente, caso contrário, digite qualquer tecla para sair: "))
            if recomecar.upper() == "S":
                cont = 3
                aleatorio=random.randint(0,10)
                os.system("cls")
            else:
                os.system("cls")
                print("Encerrando programa...")
                break
            