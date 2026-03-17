from collections import Counter
import os

qn = int(input("Digite a quantidade de notas : "))
qa = int(input("Digite a quantidade de alunos : "))

boletim = []

for i in range(qa):
    a = str(input("Qual o seu nome ?"))
    for j in range(qn):
        n = float(input(f"Digite a sua {j+1}° nota : "))
        boletim.append(n)

for i in range(qa):
    for j in range(qn):
        print(f'{boletim}')