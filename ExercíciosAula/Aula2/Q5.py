import math 
import os
from collections import Counter

m = int(input("Digite um número de elementos das listas: "))
lista1 = []
lista2 = []

for i in range(m):
    n1 = input(f"Digite o elemento {i+1} da primeira lista : ")
    lista1.append(n1)
    

for i in range(m):
    n2 = input(f"Digite o elemento {i+1} da segunda lista : ")
    lista2.append(n2)

lista3 = []

for i in range(m):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f'Lista 1 : {lista1}')
print(f'Lista 2 : {lista2}')
print(f'Lista mesclada : {lista3}')