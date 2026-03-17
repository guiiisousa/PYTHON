import math 
try:
    p = float(input("Digite seu peso em kg: "))
    a = float(input("Digite sua altura em centimetros: "))

except ValueError:
    print("Por favor, digite valores numéricos válidos.")
    exit()

def calcular_imc(peso, altura):
    imc = peso / ((altura / 100) ** 2)
    return imc

def classificar_imc(imc): 
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

print(f'Seu IMC é: {calcular_imc(p, a):.2f}')
print(f'Classificação: {classificar_imc(calcular_imc(p, a))}')



