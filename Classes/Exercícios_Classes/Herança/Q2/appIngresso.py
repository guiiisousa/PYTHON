import ingresso

while True:
    print("-" * 80)

    evento = input("Digite o nome do evento: ")
    tipo = input("Digite o tipo de ingresso (N - Normal, V - VIP): ").lower()

    valor = float(input("Digite o valor do ingresso: "))
   
    if tipo == "n":
        i = ingresso.IngressoNormal(valor, evento)

        print("\nTipo:", i.getTipoIngresso())
        print(i.toString())

    elif tipo == "v":
        adicional = float(input("Digite o valor adicional do ingresso VIP: "))

        iv = ingresso.IngressoVip(valor, evento, adicional)

        print("\nTipo:", iv.getTipoIngresso())
        print(iv.toString())

    else:
        print("Tipo de ingresso inválido!")

    continuar = input("\nDeseja cadastrar outro ingresso? (S/N): ").lower()

    if continuar != "s":
        break