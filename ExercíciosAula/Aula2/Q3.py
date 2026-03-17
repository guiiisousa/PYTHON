import math

m = int(input("Digite um número de elementos da lista: "))
lista = []
lista_nova = []

for i in range(m):
    n = int(input(f"Digite o {i+1}º número: "))
    lista.append(n)

lista_nova = lista[::-1]

print(f'Lista original : {lista}')
print(f'Lista invertida : {lista_nova}')