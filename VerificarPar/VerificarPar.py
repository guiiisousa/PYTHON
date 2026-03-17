from itertools import count
from operator import delitem

m = int(input("Digite a quantidade de elementos: "))
numeros = []

for i in range(m):
    n = int(input("Digite um número: "))
    numeros.append(n)
    
for j in range(0, len(numeros)):
    
   if numeros[j] % 2 == 0:
        print(f"{numeros[j]} é par.")
   else:        
       print(f"{numeros[j]} é ímpar.")
     