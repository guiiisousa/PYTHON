from retangulo import retangulo

b = int(input("Digite a base do retângulo: "))
a = int(input("Digite a altura do retângulo: "))

r = retangulo(b,a)

while True:

    d = input("\nDigite o que deseja calcular (area, perimetro ou diagonal): ")

    match d:
        case "area":
            print(f"A área do retângulo é: {r.areaRetangulo()}")
        case "perimetro":
            print(f"O perímetro do retângulo é: {r.perimetroRetangulo()}")
        case "diagonal":
            print(f"A diagonal do retângulo é: {r.diagonalRetangulo()}")
        case _:
            print("Opção inválida. Por favor, escolha entre 'area', 'perimetro' ou 'diagonal'.")