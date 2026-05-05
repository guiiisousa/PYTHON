#Divisão por zero#
def Dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não é permitida."
    
#Arquivo não existe#
def Ler_Arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return f"Erro: O arquivo '{nome_arquivo}' não foi encontrado."
    
#Importação de módulo#
def Importar_Modulo(nome_modulo):
    try:
        return __import__(nome_modulo)
    except ImportError:
        return f"Erro: O módulo '{nome_modulo}' não foi encontrado."

#Tipo diferente#
def Somar(a : int, b : int):
    try:
        return a + b
    except TypeError:
        return "Erro: Tipos de dados inconsistentes para soma."

##Acessar índice fora do alcance#
def Acessar_Indice(lista, indice):
    try:
        return lista[indice]
    except IndexError:
        return f"Erro: Índice {indice} fora do alcance da lista."
       
#Verficar se é uma lista#
def Verificar_Lista(lista):
    try:
        return lista.append(7)
    except ValueError:
        return "Erro: O objeto fornecido não é uma lista."

##Acessar chave inexistente#
def Acessar_Chave(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return f"Erro: A chave '{chave}' não existe no dicionário."  