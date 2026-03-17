import time 
import datetime

a = int(input("Digite o ano de nascimento: "))
m = int(input("Digite o mês de nascimento: "))
d = int(input("Digite o dia de nascimento: "))

data_nascimento = datetime.datetime(a, m, d)
data_atual = datetime.datetime.now()

soma_nascimento = data_nascimento.day + (data_nascimento.month * 30) + (data_nascimento.year*365)
soma_atual = data_atual.day + (data_atual.month * 30) + (data_atual.year*365)
idade = (soma_atual - soma_nascimento) // 365    
print(f"Você tem {idade} anos.")