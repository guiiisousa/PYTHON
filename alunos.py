def Adicionar_Aluno(boletim, nome, notas):
    boletim = {}
    boletim[nome] = []
    boletim[nome].append(notas)

def Calcular_Media(boletim, nome):

    for notas in boletim[nome]:
        if nome in boletim:
            for nota in boletim[nome][notas]:
                media = sum(boletim[nome][notas][nota]) / len(boletim[nome][notas][nota])
            return media
        else:
            print(f"O aluno {nome} não foi encontrado.")
            return None
        
def Exibir_Boletim(boletim, nome):
    if nome in boletim:
        print(f"Boletim do aluno {nome}:")
        for notas in boletim[nome]:
            print(f"  Notas: {notas}")
    