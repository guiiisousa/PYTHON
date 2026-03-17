import math 
import os
from collections import Counter

m = int(input("Digite um número de elementos da lista: "))
lista = []

for i in range(m):
    n = int(input(f"Digite o {i+1}º número: "))
    lista.append(n)

lista_limpa = list(dict.fromkeys(lista))

print(f'Lista original : {lista}')
print(f'Lista limpa : {lista_limpa}')