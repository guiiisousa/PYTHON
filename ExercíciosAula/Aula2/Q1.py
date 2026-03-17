import os 

m = int(input("Digite o número de elementos da lista: "))
lista1 = []
listaPar = []

for i in range(m):
    n = int(input(f"Digite o {i+1}º número: "))
    lista1.append(n)
    if n % 2 == 0:
        listaPar.append(n)
    
print("Lista original:", lista1)
print("Lista de números pares:", listaPar)