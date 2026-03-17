from collections import Counter

frase = "o rato roeu a roupa do rei de roma"

contagem = Counter(c for c in frase if c.isalpha())

for letra,quantidade in contagem .items():
    print(f'{letra}: {quantidade}')