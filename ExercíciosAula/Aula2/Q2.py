import os 
import math
from collections import Counter 

m = int(input("Digite um número de elementos da lista: "))
lista = []

for i in range(m):
    n = int(input(f"Digite o {i+1}º número: "))
    lista.append(n)

contagem = Counter(lista)
elemento, frequencia = contagem.most_common(1)[0]

print(f'Elemento que mais se repete : {elemento}')
print(f'Quantidade de vezes que ele se repete : {frequencia}')