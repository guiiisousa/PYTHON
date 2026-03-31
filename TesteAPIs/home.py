from brapi import *
from TesteYahooFinance import Get_history

ticket1 = input("Digite o nome do fundo: ")

print(f" "*38 + f"{ticket1.removesuffix(".SA")}")
print("-"*85)
print(Get_history(ticket1))
