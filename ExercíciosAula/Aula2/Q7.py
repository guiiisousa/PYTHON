from collections import Counter
import os

qn = int(input("Digite a quantidade de notas : "))
qa = int(input("Digite a quantidade de alunos : "))

boletim = {}

for i in range(qa):
    a = (input("Nome do aluno: "))
    boletim[a] = []
    for j in range(qn):
        n = float(input(f"Nota do(a) {a}: "))
        boletim[a].append(n)

for chave,valor in boletim.items():
    print(f"{chave}: {valor}")
    