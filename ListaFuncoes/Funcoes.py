import time 
import math
import statistics as st
import random

# Função para mostra algo na tela 
# print("")

# Função para ler um dado do usuário
# input("")

# Tipos de dados
# int(), float(), str(), bool()

# Funções matemáticas
#abs() → valor absoluto
#pow() → potência
#round() → arredondar número
#max() → maior valor
#min() → menor valor
#sum() → soma de valores

#Manipulação de listas
#len() → tamanho da lista
#sorted() → ordenar
#list() → criar lista

#Iteração
#range() → criar sequência de números
#enumerate() → obter índice e valor
#zip() → juntar listas

#Verificação
#type() → mostra o tipo da variável
#isinstance() → verifica tipo

#Manipulação de listas (dados simples)
#append() → adiciona elemento
#remove() → remove elemento
#pop() → remove pelo índice
#sort() → ordena
#reverse() → inverte
#len() → tamanho da lista

#Manipulação de dicionários
#keys() → retorna as chaves
#values() → retorna os valores
#items() → chave + valor
#get() → pega valor com segurança
#update() → atualiza dados

#Criação de funções
# def nome_da_função():
#     código da função
#     return resultado

#Funções matemáticas
# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n - 1)
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
def Media_Harmonica(n):
    if n <= 0:
        return 0
    else:
        return sum(1 / i for i in range(1, n + 1))
print(Media_Harmonica(2))