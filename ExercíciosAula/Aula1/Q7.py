import math 

n = int(input("Digite um número: "))
i = int(input("Digite a sua idade: "))

if n % 2 == 0:
    print(f"{n} é par.")
else:
    print(f"{n} é ímpar.")
    
if n > 10 and n < 20:
    print(f"{n} está entre 10 e 20.")
else:
    print(f"{n} não está entre 10 e 20.")
    
if i >= 18:
    print(f"{i} é maior de idade.")