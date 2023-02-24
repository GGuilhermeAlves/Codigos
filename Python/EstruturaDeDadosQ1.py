lista = []
for i in range(5):
  lista.append(input("Digite um número: ")) 
print("\n",lista)
print(f"\nO maior número na lista é {max(lista)} na posição {lista.index(max(lista))}\n",
      f"\nO menor número na lista é {min(lista)} na posição {lista.index(min(lista))}\n")
