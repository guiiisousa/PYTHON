from brapi import *
from yahooFinance import Get_history

ticket1 = input("Digite o nome do fundo: ")

print(Get_history(ticket1))
