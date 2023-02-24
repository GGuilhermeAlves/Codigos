lista = []
for i in range(999999):
  valor = int(input("Digite um número: "))
  if valor == 0:
    break
  else:
    lista.append(valor)
print(f"\nO maior número na lista é {max(lista)}\n")
print(lista,"\n")
