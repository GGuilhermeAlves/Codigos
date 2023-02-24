lista = []
n=str("0")
for i in range(5):
  lista.append(input("Digite um número: "))
  if n in lista:
    lista.pop(i)
    break
print("")    
print(f"O maior número na lista é {max(lista)}")
print("")
print(lista)
print("")
